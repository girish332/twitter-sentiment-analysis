import tweepy
from textblob import TextBlob

consumer_key = "FcWCZYxZk5HGAtrTi6XM4NWWB"
consumer_secret = "DpDhjGNEjiutESduvKQGRq0NVzOxverV7yGaowM1N0EKPtLypL"

access_token = "2609369311-oNLh2N8K53xTScHTRCaFZptRFWsavFbs2f1n1Kl"

access_token_secret = "2zOgJ71ik56VEY1C8yrbqyBC6gUoWsI6ogrVHQYJRNUkJ"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)

auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('narendra modi')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)

