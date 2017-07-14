# text = "trump actually believes he is a victim? Make no mistake: he is a victimizer, exploiting supporters who, like him, want someone to blame."
# text = text.lower()

# trump = ['donald', 'trump']
# hillary = ['hillary', 'clinton']

# def which_candidate():
# 	if_T = False
# 	if_H = False
# 	for name in trump:
# 		if name in text:
# 			if_T = True
# 	for name in hillary:
# 		if name in text:
# 			if_H = True

# 	print(if_T, if_H)

import nltk
from nltk.tokenize import word_tokenize

text = "If I had Donald Trump's hair I'd be cautious about running."
tokenized = word_tokenize(text)
print(tokenized)

pos = nltk.pos_tag(tokenized, tagset='universal')
print(pos)