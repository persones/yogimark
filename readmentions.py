import tweepy
from credentials import *
import os.path
import argparse

import os 
dir_path = os.path.dirname(os.path.realpath(__file__)) + "/"
print dir_path

parser = argparse.ArgumentParser(description='YogiMark')
#parser.add_argument("-t", "--notweet", help="disable tweeting", action="store_true")
args = parser.parse_args()

lastMentionFileName = dir_path + "last_mention.txt"
corpus = dir_path + "corpus.txt"
searchPhrase = "@YogiMarkov"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
if os.path.isfile(lastMentionFileName):
  with open(lastMentionFileName) as f:
    last_metnion = int(f.read())
    searchResults = api.search(searchPhrase, since_id=last_metnion);
else:
  searchResults = api.search(searchPhrase);

print len(searchResults)
if len(searchResults) == 0:
  exit()


for result in searchResults:
  tweetId = getattr(result, "id")
  authorName = getattr(getattr(result, "author"), "name")
  screenName = getattr(getattr(result, "author"), "screen_name")
  newText = getattr(result, "text").replace(searchPhrase, '').lstrip().rstrip()
  print tweetId, authorName, newText
  if getattr(result, "in_reply_to_status_id_str") == None:
    retweetText = "@" + screenName + " Thanks, " + authorName + ". I will bring this to my next practices. Namaste!"
    print retweetText 
    api.update_status(retweetText, in_reply_to_status_id = tweetId)
    with open(corpus, 'a') as f:
      f.write(str(newText) + " \n")  
  lastRetweetId = getattr(result, "id")

with open(lastMentionFileName, 'w') as f:
    f.write(str(lastRetweetId))
    
  

  
  
  
  
