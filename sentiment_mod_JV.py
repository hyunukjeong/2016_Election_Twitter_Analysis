import nltk
import pickle
from nltk.tokenize import word_tokenize


freq_JV_f = open("pickles/freq_JV.pickle", "rb")
freq_JV = pickle.load(freq_JV_f)
freq_JV_f.close()


def find_features(document):
	words = word_tokenize(document)
	features = {}
	for w in freq_JV:
		features[w] = (w in words)

	return features


open_file = open("pickles/classifier_JV.pickle", "rb")
classifier_JV = pickle.load(open_file)
open_file.close()


def sentiment(text):
	feats = find_features(text)
	return classifier_JV.classify(feats)