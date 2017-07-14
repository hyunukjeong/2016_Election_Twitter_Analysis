import tweepy
import pprint

import sentiment_mod_J as J
import sentiment_mod_JV as JV

""" Initialize tweepy with Hyun's Twitter API info """
consumer_key = 'zheeWCCzpJougMVHJ7gZTdd7p'
consumer_secret = '1HKFak8plcTzK7YZSQmUKfpHEYpvL2OjefjoMLBxUhvO6nQ7KF'
access_token = 	'828329068709937152-GPRprU6BKOIbQQ6UjT5BEdFtGWHbGe2'
access_token_secret = 'Ln5uxoG6AvSl9NtPho5H3fom4LYorAm6Yax1fKPKNyko7'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
""" End Initializing tweepy """



"""
Tweets exceeding 140 characters are truncated.
The full text of tweets are available in ['retweeted_status']['text']
"""
def show_tweet(tweet_id):
	try:
		status_json = api.get_status(tweet_id)._json
		# pprint.pprint(status_json)
		# print(status_json['text']) # This won't print full text!
		text = status_json['retweeted_status']['text']
		print(text)
		print(JV.sentiment(text))
		print("\n")
	except:
		print("access failed")

# show_tweet(787695007650213888)
# show_tweet(787695007826403329)

for tweet_id in (open('sample0_0.txt')):
	show_tweet(tweet_id)




# def store_tweets(tweet_id_txt):
# 	for tweet_id in (open(tweet_id_txt)):
# 		try:
# 			status_json = api.get_status(tweet_id)._json
# 			tweet = {}
# 			tweet['tweet_id'] = tweet_id
# 			if status_json['text']:
# 				tweet['text'] = status_json['text']
# 			tweets.insert_one(tweet)
# 		except:
# 			pass

# store_tweets('sample0_0.txt')