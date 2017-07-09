import random
import markovify
import tweepy
from credentials import *

import argparse

parser = argparse.ArgumentParser(description='YogiMark')
parser.add_argument("-t", "--notweet", help="disable tweeting", action="store_true")
args = parser.parse_args()

# create model from corpus
with open("corpus.txt") as f:
    text = f.read()
text_model = markovify.Text(text, state_size=2)
model_json = text_model.to_json()
with open("model.json", 'w') as f:
  f.write(model_json)
  
phrase = text_model.make_short_sentence(140, tries=1000)  

if args.notweet:
  print "tweeting disabled"
  print phrase
else:  
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)
  api = tweepy.API(auth)
  api.update_status(phrase)

