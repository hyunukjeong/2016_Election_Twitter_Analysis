import nltk
import pickle
from nltk.tokenize import word_tokenize


freq_J_f = open("pickles/freq_J.pickle", "rb")
freq_J = pickle.load(freq_J_f)
freq_J_f.close()


def find_features(document):
	words = word_tokenize(document)
	features = {}
	for w in freq_J:
		features[w] = (w in words)

	return features


open_file = open("pickles/classifier_J.pickle", "rb")
classifier_J = pickle.load(open_file)
open_file.close()


def sentiment(text):
	feats = find_features(text)
	return classifier_J.classify(feats)