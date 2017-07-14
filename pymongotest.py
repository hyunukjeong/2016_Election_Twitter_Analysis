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