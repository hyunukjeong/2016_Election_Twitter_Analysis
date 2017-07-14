import tweepy
import pprint
import pymongo
from pymongo import MongoClient
# import sentiment_mod_J as J
import sentiment_mod_JV as JV


""" Initialize tweepy with Hyun's Twitter API info """
consumer_key = 'put your own consumer key'
consumer_secret = 'put your own consumer secret'
access_token = 	'put your own access token'
access_token_secret = 'put your own access token secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth_handler=auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
""" End Initializing tweepy """


""" Accessing MongoDB """
client = MongoClient('localhost', 27017)
twitter_db = client['twitter_db']
T_tweets = twitter_db['T_tweets']
H_tweets = twitter_db['H_tweets']


""" Method for determining if tweet is about Trump or Hillary """
trump = ['donald', 'trump']
hillary = ['hillary', 'clinton']

def which_candidate(text):
	lower_text = text.lower()
	if_T = False
	if_H = False
	for name in trump:
		if name in lower_text:
			if_T = True
	for name in hillary:
		if name in lower_text:
			if_H = True
	return (if_T, if_H)

""" Store Tweets """
def store_tweets(tweet_id_txt):
	for tweet_id in (open(tweet_id_txt)):
		try:
			status_json = api.get_status(tweet_id)._json
			if status_json['retweeted_status']:
				text = status_json['retweeted_status']['text']
			else:
				text = status_json['text']
			tweet = {}
			tweet['tweet_id'] = tweet_id
			if status_json['text']:
				tweet['text'] = text
			tweet['sentiment'] = JV.sentiment(text)
			candidate = which_candidate(text)
			# print(candidate)
			if candidate[0] and not candidate[1]: #Trump tweet
				T_tweets.insert_one(tweet)
			elif candidate[1] and not candidate[0]: #Hillary tweet
				H_tweets.insert_one(tweet)
		except:
			pass

def test_get(tweet_id):
	# status = api.get_status(tweet_id).retweeted_status
	# pprint.pprint(status)
	status_json = api.get_status(tweet_id)._json
	pprint.pprint(status_json)
	# print(status_json['retweeted_status']['text'])



def printRows(collection):
	for item in collection.find():
		pprint.pprint(item)


store_tweets('sample12.txt')
# test_get(787695101564727296)