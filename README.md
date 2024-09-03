
# **Sentiment Analysis Trading Bot**

## **Overview & Findings**

This project implements an automated trading bot that leverages sentiment analysis of Twitter data to make trading decisions on the Alpaca platform. The bot continuously scrapes tweets based on specific keywords, performs sentiment analysis using a custom-trained Naive Bayes classifier, and dynamically adjusts a stock portfolio by placing buy or sell orders based on the aggregated sentiment. The bot executes a long-short equity trading strategy, making it responsive to market sentiment reflected in social media.

After running this bot for a time period of 7 weeks here are some observed key metrics: 

- Initial Portfolio Value: $5,000
- Final Portfolio Value: $5,730
- Total Profit: $730
- Return on Investment (ROI): 14.6%
- Average Weekly Return: 2.08%
- Total Number of Trades: 152
- Long Positions: 81
- Short Positions: 71
- Win Rate: 62% (94 winning trades, 58 losing trades)

Although this seems good, these results are unlikley to mirror real world trades due to a host of reasons including market latency and limited data scope. Nonetheless, it was a fun project to implement.

## **Features**

- **Real-time Tweet Scraping**: Uses the Tweepy library to fetch and filter tweets in real-time based on user-defined keywords.
- **Sentiment Analysis**: A Naive Bayes classifier trained with NLTK is employed to classify tweets as positive or negative, guiding trading decisions.
- **Automated Trading**: Trades are executed on the Alpaca platform using the Alpaca Trade API, allowing for both paper and live trading.
- **Long-Short Equity Strategy**: The bot dynamically rebalances the portfolio based on the sentiment analysis, going long on stocks with positive sentiment and short on stocks with negative sentiment.

## **Project Structure**

### **1. Configuration File (`config.py`)**

- **Purpose**: Centralizes the API keys and configuration settings for the project.
- **Contents**:
  - **Twitter API Credentials**: Used for authenticating the Tweepy API to scrape tweets.
  - **Alpaca API Credentials**: Required for executing trades on Alpaca's platform.
  - **Keywords**: List of keywords to search for on Twitter.
  - **Default Trading Parameters**: Includes stock symbols (e.g., `AAPL`) and order values.

### **2. Tweet Scraper (`tweet_scraper.py`)**

- **Purpose**: Scrapes tweets in real-time using the Tweepy API and cleans the tweet text.
- **Implementation**:
  - **Class `TweetScraper`**: Handles Twitter API authentication and tweet fetching.
  - **`get_tweets` Method**: Fetches tweets based on keywords and removes retweets and newline characters.

### **3. Sentiment Analysis (`classifier.py`)**

- **Purpose**: Trains a Naive Bayes classifier for sentiment analysis and classifies the sentiment of tweets.
- **Implementation**:
  - **Data Preprocessing**: Uses NLTK to tokenize and clean tweet text, removing noise and applying lemmatization.
  - **Model Training**: Trains a Naive Bayes classifier using a labeled dataset of positive and negative tweets from `nltk.corpus.twitter_samples`.
  - **Classification**: Classifies new tweets as either positive or negative, based on their tokenized content.

### **4. Trading Execution (`alpaca_trader.py`)**

- **Purpose**: Executes trades on the Alpaca platform based on the sentiment analysis results.
- **Implementation**:
  - **Alpaca API Initialization**: Authenticates and initializes the Alpaca API for trading.
  - **Sentiment Integration**:
    - **`get_sentiment` Method**: Aggregates sentiment from a batch of tweets and returns counts of positive and negative sentiments.
  - **Long-Short Equity Strategy**:
    - **`stocks_long_short` Method**: Decides which stocks to long or short based on the sentiment analysis.
  - **Portfolio Rebalancing**:
    - **`rebalance_portfolio` Method**: Cancels existing orders, closes positions, and submits new market orders for long and short positions.
    - Implements error handling with `try-except` blocks and provides feedback on successful or failed trades.
  - **Main Execution Loop**: Continuously monitors the market and rebalances the portfolio every hour.

## **Trading Strategy**

- **Long-Short Equity**: 
  - The bot implements a long-short equity strategy, which involves taking long positions in stocks with positive sentiment and short positions in stocks with negative sentiment. This strategy aims to capitalize on market sentiment by buying undervalued stocks (positive sentiment) and selling overvalued ones (negative sentiment).
  - **Risk Management**: The portfolio is periodically rebalanced to align with the latest sentiment analysis, ensuring that the exposure to risk is dynamically adjusted.

## **Installation**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/sentiment-analysis-trading-bot.git
   cd sentiment-analysis-trading-bot
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r Requirements.txt
   ```

3. **Set Up Configuration**:
   - Replace the placeholders in `config.py` with your Twitter and Alpaca API credentials.

## **Usage**

1. **Run the Bot**:
   ```bash
   python alpaca_trader.py
   ```
   - The bot will start scraping tweets, perform sentiment analysis, and execute trades on the Alpaca platform.

2. **Monitor Trades**:
   - Check the Alpaca dashboard or console output to monitor the trades being executed based on sentiment analysis.

## **Contributing**

- Contributions are welcome! Feel free to submit a pull request or open an issue if you find any bugs or have suggestions for new features.

## **License**

- This project is licensed under the MIT License.

## **Disclaimer**

- **Paper Trading**: It's highly recommended to start with Alpaca's paper trading environment to avoid real financial risks while testing the bot.
- **Not Financial Advice**: This bot is for educational purposes only and should not be considered financial advice. Use at your own risk.
