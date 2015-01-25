import sys
import json

'''
Usage: ipython top_ten.py out_twitter_stream.txt
'''

def read_tweets(tweet_file):
    hashtags = [] 
    for line in open(tweet_file):
       try:
          for i in json.loads(line).get('entities','')['hashtags']:
              hashtags.append( i['text'])
       except:
          pass
    return hashtags
    
    
def main():
    hashtags = read_tweets(sys.argv[1])
    sethashtags = set(hashtags)
    counts = [hashtags.count(el) for el in sethashtags]
    indices = [i[0] for i in sorted(enumerate(counts), reverse=True, key=lambda x:x[1])]
    top_ten_indices = indices[0:10]
    for index in top_ten_indices:
        print list(sethashtags)[index], counts[index]
if __name__ == '__main__':
    main()
