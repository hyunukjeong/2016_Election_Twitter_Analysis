import tweepy
import pprint
import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
twitter_db = client['twitter_db']
T_tweets = twitter_db['T_tweets']
H_tweets = twitter_db['H_tweets']

def printRows(collection):
	for item in collection.find():
		pprint.pprint(item)


""" CAREFUL DON'T UNCOMMENT UNLESS YOU ARE SURE!!!! """
##### T_tweets.drop()
##### H_tweets.drop()
""" CAREFUL DON'T UNCOMMENT UNLESS YOU ARE SURE!!!! """

##### Results #####
# print("TRUMP")
# print(T_tweets.count())
# T_pos = T_tweets.find({'sentiment': 'pos'})
# T_neg = T_tweets.find({'sentiment': 'neg'})
# print(T_pos.count(), T_neg.count())
# print("END TRUMP")
# print("\n")

# print("HILLARY")
# print(H_tweets.count())
# H_pos = H_tweets.find({'sentiment': 'pos'})
# H_neg = H_tweets.find({'sentiment': 'neg'})
# print(H_pos.count(), H_neg.count())
# print("END HILLARY")
# print("\n")
##### End of Results #####

print("HILLARY")
tweet = H_tweets.find_one()
print(tweet)



# T_pos = T_tweets.find({'sentiment':'pos'})
# for i in range(10):
# 	print(T_pos[i+2500]['text'])
# 	print("\n")

# print("============================")
# T_neg = T_tweets.find({'sentiment':'neg'})
# for i in range(10):
# 	print(T_neg[i+2500]['text'])
# 	print("\n")











# """Initialize tweepy"""
# consumer_key = 'zheeWCCzpJougMVHJ7gZTdd7p'
# consumer_secret = '1HKFak8plcTzK7YZSQmUKfpHEYpvL2OjefjoMLBxUhvO6nQ7KF'
# access_token = 	'828329068709937152-GPRprU6BKOIbQQ6UjT5BEdFtGWHbGe2'
# access_token_secret = 'Ln5uxoG6AvSl9NtPho5H3fom4LYorAm6Yax1fKPKNyko7'

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)

# api = tweepy.API(auth)
# """End Initializing tweepy"""


# """Accessing MongoDB"""
# client = MongoClient('localhost', 27017)
# db = client['twitter_db']
# # db.collection_names()
# tweet_collection = db['tweet_collection']


# def collectTweets(tweet_id_txt):
# 	for tweet_id in (open(tweet_id_txt)):
# 		try:
# 			status_json = api.get_status(tweet_id)._json
# 			tweet = {}
# 			if status_json['text']:
# 				tweet['text'] = status_json['text']
# 			if status_json['user']['location']:
# 				tweet['location'] = status_json['user']['location']
# 			# pprint.pprint(tweet)
# 			tweet_collection.insert_one(tweet)
# 		except:
# 			pass
# 			# print("failed")


# # collectTweets('sample0_0.txt')

# print('print collections')
# db.collection_names()
# pprint.pprint(tweet_collection.find_one())