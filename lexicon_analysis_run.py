import pymongo
from pymongo import MongoClient
import pickle
from lexicon_analysis import *

client = MongoClient('localhost', 27017)
twitter_db = client['twitter_db']
T_tweets = twitter_db['T_tweets']
H_tweets = twitter_db['H_tweets']

def printRows(collection):
	for item in collection.find():
		pprint.pprint(item)

pos_f = open("pickles/pos.pickle", "rb")
pos = pickle.load(pos_f)
pos_f.close()

neg_f = open("pickles/neg.pickle", "rb")
neg = pickle.load(neg_f)
neg_f.close()