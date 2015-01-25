import sys
import json


"""
Usage: ipython frequency.py <tweet_file>
"""

def read_tweets(tweet_file):
    tweets = [] 
    for line in open(tweet_file):
       try:
          tweets.append(json.loads(line).get('text',''))
       except:
          pass
    return tweets

def getwords(tweets):
    words = []
    for tweet in tweets:
        for word in tweet.split():
            words.append(word)
    return list(set(words))

def getwordcount(tweets, word): #total word count in all tweets
    counts = 0.
    for tweet in tweets:
        if word in tweet.split():
           counts = counts+1. 
    return counts

def main():
    tweets = read_tweets(sys.argv[1])
    words = getwords(tweets)
    num_words = len(words)
    for word in words:
        print word, getwordcount(tweets, word)/num_words
             
if __name__ == '__main__':
    main()

