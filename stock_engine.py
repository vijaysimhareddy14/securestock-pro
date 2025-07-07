# stock_engine.py

import yfinance as yf
import pandas as pd
from config import VOLUME_THRESHOLD
from sentiment_engine import fetch_headlines, analyze_sentiment, get_threat_level

def fetch_stock_data(ticker):
    data = yf.download(ticker, period="3mo", interval="1d")

    if len(data) < 50:
        return pd.DataFrame()

    data['SMA_50'] = data['Close'].rolling(50).mean()
    data['Volume_Ratio'] = data['Volume'] / data['Volume'].rolling(20).mean()
    
    return data.tail(1).reset_index(drop=True)

def screen_stock(ticker):
    df = fetch_stock_data(ticker)

    if df.empty or df.isnull().values.any():
        return {
            "ticker": ticker,
            "price": "N/A",
            "sma50": "N/A",
            "volume_ratio": "N/A",
            "screened_in": False,
            "sentiment": "N/A",
            "threat_level": "⚪ Unknown"
        }

    row = df.iloc[0]

    try:
        close = row['Close'].item()
        sma = row['SMA_50'].item()
        volume_ratio = row['Volume_Ratio'].item()

        decision = close > sma and volume_ratio > VOLUME_THRESHOLD

        # NEW: Sentiment + Threat
        headlines = fetch_headlines(ticker)
        sentiment_score = analyze_sentiment(headlines)
        threat_level = get_threat_level(sentiment_score)

        return {
            "ticker": ticker,
            "price": round(close, 2),
            "sma50": round(sma, 2),
            "volume_ratio": round(volume_ratio, 2),
            "screened_in": decision,
            "sentiment": sentiment_score,
            "threat_level": threat_level
        }

    except Exception:
        return {
            "ticker": ticker,
            "price": "N/A",
            "sma50": "N/A",
            "volume_ratio": "N/A",
            "screened_in": False,
            "sentiment": "N/A",
            "threat_level": "⚪ Unknown"
        }
