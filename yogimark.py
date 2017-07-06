import random
import markovify
import tweepy
from credentials import *

# Get raw text as string.
with open("corpus.txt") as f:
    text = f.read()

text_model = markovify.Text(text, state_size=2)
phrase = text_model.make_short_sentence(140, tries=1000)
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
api.update_status(phrase)

