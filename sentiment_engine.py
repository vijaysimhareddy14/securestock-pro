# sentiment_engine.py
from config import NEWS_API_KEY
import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

##NEWS_API_KEY = "YOUR_API_KEY"  # 🔁 Replace with your NewsAPI key

def fetch_headlines(ticker):
    url = f"https://newsapi.org/v2/everything?q={ticker}&sortBy=publishedAt&apiKey={NEWS_API_KEY}&language=en"
    response = requests.get(url)
    
    if response.status_code != 200:
        return []

    articles = response.json().get("articles", [])
    return [article["title"] for article in articles[:5]]

def analyze_sentiment(headlines):
    analyzer = SentimentIntensityAnalyzer()
    scores = []

    for h in headlines:
        score = analyzer.polarity_scores(h)['compound']
        print(f"📰 {h} -> Score: {score}")
        scores.append(score)

    if not scores:
        return 0.0

    return round(sum(scores) / len(scores), 2)

def get_threat_level(score):
    if score < -0.4:
        return "🔴 High"
    elif score < 0:
        return "🟡 Medium"
    else:
        return "🟢 Low"
