from __future__ import division
import sys
import json

"""
Usage: ipython gms_term_sentiment.py AFINN-111.txt out_twitter_stream.txt 

"""

def read_sent(afinnfile):
   afinnfile = open(afinnfile)
   scores = {} # initialize an empty dictionary
   for line in afinnfile.readlines():
       term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
       scores[term] = int(score)  # Convert the score to an integer.
   return scores

def read_tweets(tweet_file):
    tweets = [] 
    for line in open(tweet_file):
       try:
          tweets.append(json.loads(line).get('text',''))
       except:
          pass
    return tweets
    
#Affin words   
def getscores(scores, tweet):
    sum = 0.0
    for word in tweet.split():
        sum += scores.get(word,0) 
    return sum

#Non-dict words
def getmorewords(scores, tweet):
    nonword_words = []
    for word in tweet.split():
        if word not in scores.keys():
           nonword_words.append(word)
    return list(set(nonword_words))

def makeUpscores(scores, tweets, nonword_word): #Assign snetiment scores
    nonword_score = 0.
    freq = 0.
    for tweet in tweets:
        score = getscores(scores, tweet)   
        if nonword_word in tweet.split():
           freq = freq + 1. #tweet.split().count(nonword_word)
           nonword_score = nonword_score + score  
    if freq != 0.:        
       avgscore = nonword_score/freq
    else:
       avgscore = 0.
    return avgscore


def main():
    tweets = read_tweets(sys.argv[2])
    scores = read_sent(sys.argv[1])
    new_words = []
    for tweet in tweets:
        new_words = new_words + getmorewords(scores, tweet)
    new_words = list(set(new_words))
    for new_word in new_words:
        new_score = makeUpscores(scores, tweets[0], new_word) 
        print new_word, new_score 
         
if __name__ == '__main__':
    main()
