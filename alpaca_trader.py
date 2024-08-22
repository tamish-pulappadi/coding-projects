from nltk.tokenize import word_tokenize
from time import sleep
import alpaca_trade_api as tradeapi
from classifier import classify_tweet, train_classifier
from tweet_scraper import TweetScraper
import config

api = tradeapi.REST(config.alpaca_key, config.alpaca_secret, 'https://paper-api.alpaca.markets', api_version='v2')

def get_sentiment(keyword, num_tweets, date_since=None):
    scraper = TweetScraper()
    tweets = scraper.get_tweets(keyword, num_tweets, date_since)
    classifier = train_classifier()
    
    positive_count = 0
    negative_count = 0
    
    for tweet in tweets:
        sentiment = classify_tweet(classifier, tweet)
        if sentiment == "Positive":
            positive_count += 1
        else:
            negative_count += 1
    
    return {"Positive": positive_count, "Negative": negative_count}

def stocks_long_short(tweet_qty):
    sentiment = get_sentiment('AAPL', tweet_qty)
    
    long_stocks = []
    short_stocks = []
    
    if sentiment['Positive'] > sentiment['Negative']:
        long_stocks.append('AAPL')
    else:
        short_stocks.append('AAPL')
    
    return long_stocks, short_stocks

def rebalance_portfolio(long_stocks, short_stocks, order_value):
    api.cancel_all_orders()
    api.close_all_positions()
    
    for stock in long_stocks:
        try:
            latest_close = api.get_barset(stock['ticker'], 'minute', limit=1)[stock['ticker']][0].c
            order_qty = round(order_value / latest_close)
            api.submit_order(stock['ticker'], qty=order_qty, side='buy', type='market', time_in_force='day')
        except:
            print(f"Failed to buy {stock['company']}!")
    
    for stock in short_stocks:
        try:
            latest_close = api.get_barset(stock['ticker'], 'minute', limit=1)[stock['ticker']][0].c
            order_qty = round(order_value / latest_close)
            api.submit_order(stock['ticker'], qty=order_qty, side='sell', type='market', time_in_force='day')
        except:
            print(f"Failed to sell {stock['company']}!")
    
    print("\nStocks have been ordered, and your portfolio has been re-balanced.")
