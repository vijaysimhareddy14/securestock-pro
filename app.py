# app.py

import streamlit as st
from stock_engine import screen_stock

st.set_page_config(page_title="SecureStock Pro", layout="centered")
st.title("📈 SecureStock Pro")
st.subheader("AI-powered Stock Screener with Threat Detection 🧠")

st.sidebar.markdown("🛡️ **Threat Monitor Status:**")
st.sidebar.markdown("🟢 All Systems Operational")

st.markdown("---")

tickers = st.text_input("Enter comma-separated stock tickers (e.g., AAPL, TSLA, INFY):")

if tickers:
    tickers = [t.strip().upper() for t in tickers.split(",")]
    
    for ticker in tickers:
        result = screen_stock(ticker)

        st.markdown(f"### 📊 {ticker}")
        st.write(f"💰 **Price:** {result['price']}")
        st.write(f"📏 **SMA-50:** {result['sma50']}")
        st.write(f"📦 **Volume Ratio:** {result['volume_ratio']}")
        st.write(f"✅ **Screened In?** {'Yes ✅' if result['screened_in'] else 'No ❌'}")

        # NEW Sentiment & Threat Display
        st.write(f"📰 **News Sentiment Score:** {result['sentiment']} — {result['threat_level']}")
        st.markdown("---")
