# Sentiment Analysis on Tweets Related to 2016 US Presidential Election

## Link to tweet ID data:

https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi%3A10.7910%2FDVN%2FPDI7IN


## Programming Language ##
* Python 3

## List of Libraries Needed ##
* NLTK
* Tweepy
* PyMongo

### I got much help from the following tutorial: ###
https://www.youtube.com/watch?v=FLZvOKSCkxY&list=PLQVvvaa0QuDf2JswnfiGkliBInZnIC4HL

### Notes & Instructions ###
* Download tweet ID's from the link above
* Donwload the training dataset by following p.18 of the tutorial above
* You will have to sign up on Twitter to get your own keys to use Twitter API
* You can test the Twitter API using tweepytest.py
* Create subdirectories called 'short_reviews' and 'pickles'
* Build the classifier by uncommenting and running the code step by step in pickling.py (Some steps will take very long time)
* save_tweets.py sets up MongoDB and stores tweets in the database
* Use pymongotest.py to query data


