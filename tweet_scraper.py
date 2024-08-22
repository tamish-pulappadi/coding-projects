import tweepy as tw
import config

class TweetScraper:
    
    def __init__(self):
        self.login()
    
    def login(self):
        auth = tw.OAuthHandler(config.consumer_key, config.consumer_secret)
        auth.set_access_token(config.secret_key, config.secret_secret)
        self.api = tw.API(auth, wait_on_rate_limit=True)
    
    def get_tweets(self, keyword, tweet_number, date_since=None):
        search_words = f"{keyword} -filter:retweets"
        tweets = tw.Cursor(self.api.search, q=search_words, lang="en", since=date_since, tweet_mode='extended').items(tweet_number)
        tweet_list = [tweet.full_text.replace('\n', ' ') for tweet in tweets]
        
        for t in tweet_list:
            print(t, '\n')
        
        return tweet_list

if __name__ == "__main__":
    t = TweetScraper()
    t.get_tweets('apple', 10)
