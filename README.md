# 📈 SecureStock Pro

**AI-powered Stock Screener with Real-Time Threat Detection**

SecureStock Pro is a smart financial analysis tool that helps analysts and investors screen stocks using technical indicators (like SMA & Volume Ratio) alongside real-time sentiment and threat analysis from recent news.

> 🚀 Built with Python, Streamlit, yFinance, and NLP (VADER)

---

## 🔍 Features

- ✅ **SMA-50 Technical Screening**: Screens stocks whose price crosses above their 50-day Simple Moving Average.
- ✅ **Volume Spike Detection**: Filters based on unusual trading volume ratio.
- 🧠 **News Sentiment Analysis**: Uses NLP to compute sentiment score from top 5 news headlines.
- 🛡️ **Threat Level Categorization**: Classifies stocks into Low, Medium, or High risk based on news sentiment.
- 💻 **Streamlit UI**: Clean, interactive dashboard to enter tickers and visualize results instantly.



## 🧠 How It Works

### 📊 Technical Indicators
- `Price > SMA_50` → potential breakout
- `Volume_Ratio > 1.5` → abnormal trading activity

### 📰 News Sentiment (VADER)
- Sentiment score aggregated from top 5 headlines via NewsAPI
- Threat Levels:
  - 🔴 High: score < -0.4
  - 🟡 Medium: score < 0
  - 🟢 Low: score ≥ 0

---

## 🚀 Usage

### 🔧 Install Dependencies

```bash
pip install -r requirements.txt

🔐 Set Up Config

Create a config.py file in the root directory:
NEWS_API_KEY = "your_newsapi_key_here"
VOLUME_THRESHOLD = 1.5

✅ requirements.txt

streamlit==1.35.0
yfinance==0.2.40
pandas==2.2.2
requests==2.32.3
vaderSentiment==3.3.2
Run the App
streamlit run app.py

🖥️ Sample Output

Ticker: TSLA
💰 Price: $315.35
📏 SMA-50: $297.84
📦 Volume Ratio: 1.62
✅ Screened In: Yes ✅
📰 Sentiment Score: -0.32
🛡️ Threat Level: 🟡 Medium


📚 Technologies Used

.Python 🐍

.Streamlit

.yFinance

.NewsAPI

.VADER Sentiment (NLP)

.Git/GitHub

👨‍💼 Ideal For

.💼 Goldman Sachs / Quantitative Analyst Prep
.📊 Finance + AI portfolios
.📈 Investment strategy automation

🙌 Author

Vijay Simha Reddy
