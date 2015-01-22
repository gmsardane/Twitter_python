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
    
   
def getscores(scores, tweet):
    sum = 0.0
    for word in tweet.split():
        sum += scores.get(word,0)   
    return sum


def main():
    tweets = read_tweets(sys.argv[2])
    scores = read_sent(sys.argv[1])
    for tweet in tweets:
        print getscores(scores, tweet) 
  
if __name__ == '__main__':
    main()







#def hw():
#    print 'Hello, world!'
#
#def lines(fp):
#    print str(len(fp.readlines()))
 
    #hw()
    #lines(sent_file)   #lines in sentiments file AFINN 
    #lines(tweet_file)  #Lines in tweet file
