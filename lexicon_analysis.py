import pickle

##### Pickle Lexicons #####
# all_words=[]
# all_polarity=[]

# for line in (open('polarity_lexicon.txt')):
# 	line_after_split=line.split(' ')
# 	all_words.append(line_after_split[2])
# 	all_polarity.append(line_after_split[-1])

# print(len(all_words))
# print(len(all_polarity))

# all_words_2=[]
# for i in range(8222):
#     all_words_2.append(all_words[i][6:])

# all_polarity_2=[]
# for i in all_polarity:
# 	all_polarity_2.append(i[:-1])

# all_polarity_3=[]
# for i in all_polarity_2:
# 	all_polarity_3.append(i[14:])

# pos=[]
# neg=[]
# neutral=[]
# for i in range(8222):
# 	if all_polarity_3[i]=='positive':
# 		pos.append(all_words_2[i])
# 	elif all_polarity_3[i]=='negative':
# 		neg.append(all_words_2[i])
# 	else:
# 		neutral.append(all_words_2[i])

# save_pos = open("pickles/pos.pickle","wb")
# pickle.dump(pos, save_pos)
# save_pos.close()

# save_neg = open("pickles/neg.pickle","wb")
# pickle.dump(neg, save_neg)
# save_neg.close()

##### End Pickling Lexicons #####

##### Load pickled lexicons #####
# pos_f = open("pickles/pos.pickle", "rb")
# pos = pickle.load(pos_f)
# pos_f.close()

# neg_f = open("pickles/neg.pickle", "rb")
# neg = pickle.load(neg_f)
# neg_f.close()
##### End loading pickled lexicons #####


candidate_1=['hillary','clinton']
candidate_2=['donald','trump']

def if_mentions_sentiment(sample):
	for_1=0 
	for_2=0
	against_1=0
	against_2=0
	for tweet in sample:
		if_1=False
		if_2=False
		#print tweet
		for term in candidate_1:
			if if_1==False and term in tweet:
				if_1=True
		for term in candidate_2:
			if if_2==False and term in tweet:
				if_2=True
		if if_1==False and if_2==True:
			count_pos=0
			count_neg=0
			tokened = token_tweet(tweet)
			for word in tokened:
				if word in pos:
					count_pos += 1
				elif word in neg:
					count_neg += 1  
			if count_pos>count_neg:
				for_2 += 1
				print("pos 2")
				print(tokened)
			elif count_pos<count_neg:
				against_2 += 1
				print("neg 2")
				print(tokened)
		elif if_1==True and if_2==False:
			count_pos=0
			count_neg=0
			tokened = token_tweet(tweet)
			for word in tokened:
				if word in pos:
					count_pos += 1
				elif word in neg:
					count_neg += 1  
			if count_pos>count_neg:
				for_1 += 1
			elif count_pos<count_neg:
				against_1 += 1
			
	return(for_1,for_2,against_1,against_2)

import re
emoticons_str = r"""
	(?:
		[:=;] # Eyes
		[oO\-]? # Nose (optional)
		[D\)\]\(\]/\\OpP] # Mouth
	)"""
 
regex_str = [
	emoticons_str,
	r'<[^>]+>', # HTML tags
	r'(?:@[\w_]+)', # @-mentions
	r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
	r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
	r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
	r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
	r'(?:[\w_]+)', # other words
	r'(?:\S)' # anything else
]

tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
 
def tokenize(s):
	return tokens_re.findall(s)
 
def preprocess(s, lowercase=False):
	tokens = tokenize(s)
	if lowercase:
		tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
	return tokens

def token_tweet(t):
	return tokens_re.findall(t)

print(if_mentions_sentiment(text_list))