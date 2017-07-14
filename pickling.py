import nltk
import random

import pickle

from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist


##### STEP 1 #####

# # open reviews
# short_pos = open("short_reviews/positive.txt", "r", encoding='UTF-8').read()
# short_neg = open("short_reviews/negative.txt", "r", encoding='UTF-8').read()

# ### Initialize lists ###
# documents = [] # list of tuples (review, category)
# all_J = [] # list of all adjectives in the reviews
# all_JV = [] # list of all adjectives and verbs in the reviews


# for p in short_pos.split('\n'):
# 	documents.append( (p, "pos") ) # push all reviews to documents list
# 	words = word_tokenize(p) # word_tokenize each sentence
# 	pos = nltk.pos_tag(words) # part of speech tag
# 	for w in pos:
# 		if w[1][0]=="J":
# 			all_J.append(w[0].lower())
# 			all_JV.append(w[0].lower())
# 		elif w[1][0]=="V":
# 			all_JV.append(w[0].lower())

# for p in short_neg.split('\n'):
# 	documents.append( (p, "neg") )
# 	words = word_tokenize(p)
# 	pos = nltk.pos_tag(words)
# 	for w in pos:
# 		if w[1][0]=="J":
# 			all_J.append(w[0].lower())
# 			all_JV.append(w[0].lower())
# 		elif w[1][0]=="V":
# 			all_JV.append(w[0].lower())


# ### Pickle documents ###
# save_documents = open("pickles/documents.pickle","wb")
# pickle.dump(documents, save_documents)
# save_documents.close()

# ### Pickle all_J and all_JV ###
# save_all_J = open("pickles/all_J.pickle","wb")
# pickle.dump(all_J, save_all_J)
# save_all_J.close()

# save_all_JV = open("pickles/all_JV.pickle","wb")
# pickle.dump(all_JV, save_all_JV)
# save_all_JV.close()



##### STEP 2 #####

# documents_f = open("pickles/documents.pickle", "rb")
# documents = pickle.load(documents_f)
# documents_f.close()

# all_J_f = open("pickles/all_J.pickle", "rb")
# all_J = pickle.load(all_J_f)
# all_J_f.close()

# all_JV_f = open("pickles/all_JV.pickle", "rb")
# all_JV = pickle.load(all_JV_f)
# all_JV_f.close()


# freq_J = []
# freq = FreqDist(all_J)
# f_common = freq.most_common(5000)
# for w in f_common:
# 	freq_J.append(w[0])

# freq_JV = []
# freq = FreqDist(all_JV)
# f_common = freq.most_common(10000)
# for w in f_common:
# 	freq_JV.append(w[0])


# save_freq_J = open("pickles/freq_J.pickle","wb")
# pickle.dump(freq_J, save_freq_J)
# save_freq_J.close()

# save_freq_JV = open("pickles/freq_JV.pickle","wb")
# pickle.dump(freq_JV, save_freq_JV)
# save_freq_JV.close()


##### STEP 3 #####

# documents_f = open("pickles/documents.pickle", "rb")
# documents = pickle.load(documents_f)
# documents_f.close()

# freq_J_f = open("pickles/freq_J.pickle", "rb")
# freq_J = pickle.load(freq_J_f)
# freq_J_f.close()

# freq_JV_f = open("pickles/freq_JV.pickle", "rb")
# freq_JV = pickle.load(freq_JV_f)
# freq_JV_f.close()

# print(len(freq_J))
# print(len(freq_JV))

# def find_features(document, word_list):
# 	words = word_tokenize(document)
# 	features = {}
# 	for w in word_list:
# 		features[w] = (w in words)

# 	return features


# featuresets_J = [(find_features(rev, freq_J), category) for (rev, category) in documents]
# random.shuffle(featuresets_J)
# print(len(featuresets_J))

# save_featuresets_J = open("pickles/featuresets_J.pickle","wb")
# pickle.dump(featuresets_J, save_featuresets_J)
# save_featuresets_J.close()


# featuresets_JV = [(find_features(rev, freq_JV), category) for (rev, category) in documents]
# random.shuffle(featuresets_JV)
# print(len(featuresets_JV))

# save_featuresets_JV = open("pickles/featuresets_JV.pickle","wb")
# pickle.dump(featuresets_JV, save_featuresets_JV)
# save_featuresets_JV.close()



##### STEP 4 ##### Classifier_J

# featuresets_J_f = open("pickles/featuresets_J.pickle", "rb")
# featuresets_J = pickle.load(featuresets_J_f)
# featuresets_J_f.close()

# random.shuffle(featuresets_J)

# testing_set_J = featuresets_J[5000:]
# training_set_J = featuresets_J[:5000]

# classifier_J = nltk.NaiveBayesClassifier.train(training_set_J)
# print("Original Naive Bayes Algo accuracy percent:", (nltk.classify.accuracy(classifier_J, testing_set_J)*100))
# classifier_J.show_most_informative_features(20)

# Train with the entire featuresets_J and pickle the classifier
# classifier_J = nltk.NaiveBayesClassifier.train(featuresets_J)
# classifier_J.show_most_informative_features(20)

# save_classifier_J = open("pickles/classifier_J.pickle","wb")
# pickle.dump(classifier_J, save_classifier_J)
# save_classifier_J.close()

##### STEP 5 ##### Classifier_JV

# featuresets_JV_f = open("pickles/featuresets_JV.pickle", "rb")
# featuresets_JV = pickle.load(featuresets_JV_f)
# featuresets_JV_f.close()

# random.shuffle(featuresets_JV)

# testing_set_JV = featuresets_JV[5000:]
# training_set_JV = featuresets_JV[:5000]

# classifier_JV = nltk.NaiveBayesClassifier.train(training_set_JV)
# print("Original Naive Bayes Algo accuracy percent:", (nltk.classify.accuracy(classifier_JV, testing_set_JV)*100))
# classifier_JV.show_most_informative_features(20)

# Train with the entire featuresets_J and pickle the classifier
# classifier_JV = nltk.NaiveBayesClassifier.train(featuresets_JV)
# classifier_JV.show_most_informative_features(20)

# save_classifier_JV = open("pickles/classifier_JV.pickle","wb")
# pickle.dump(classifier_JV, save_classifier_JV)
# save_classifier_JV.close()