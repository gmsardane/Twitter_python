from __future__ import division
from geopy.geocoders import Nominatim
import sys
import json
import geopy

"""
ipython happiest_state.py AFINN-111.txt out_twitter_stream.txt 
"""

def read_sent(afinnfile):
   afinnfile = open(afinnfile)
   scores = {} # initialize an empty dictionary
   for line in afinnfile.readlines():
       term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
       scores[term] = int(score)  # Convert the score to an integer.
   return scores


def getscores(scores, tweet):
    sum = 0.0
    for word in tweet.split():
        sum += scores.get(word,0)   
    return sum


def read_tweets_USA(tweet_file):
    geolocator = Nominatim() 
    USA_add=[]
    USA_tweets_scores = [] 
    scores = read_sent(sys.argv[1])
    for line in open(tweet_file): 
       try:

          if json.loads(line).get('coordinates') != None:
             locations = json.loads(line).get('coordinates','')
             tweet = json.loads(line).get('text','')
             loc = geolocator.reverse(str(locations['coordinates'][1])+','+\
          str(locations['coordinates'][0])) 
             if loc.address[-24:] == 'United States of America':
                USA_add.append(loc.address)
                USA_tweets_scores.append(getscores(scores, tweet))
       except:
          pass
    return [USA_add, USA_tweets_scores]


def main():  

    USA_add, USA_tweet_scores = read_tweets_USA(sys.argv[2])
    states = {\
        'AK': 'Alaska',     \
        'AL': 'Alabama',\
        'AR': 'Arkansas',\
        'AS': 'American Samoa',\
        'AZ': 'Arizona',\
        'CA': 'California',\
        'CO': 'Colorado',\
        'CT': 'Connecticut',\
        'DC': 'District of Columbia',\
        'DE': 'Delaware',\
        'FL': 'Florida',\
        'GA': 'Georgia',\
        'GU': 'Guam',\
        'HI': 'Hawaii',\
        'IA': 'Iowa',\
        'ID': 'Idaho',\
        'IL': 'Illinois',\
        'IN': 'Indiana',\
        'KS': 'Kansas',\
        'KY': 'Kentucky',\
        'LA': 'Louisiana',\
        'MA': 'Massachusetts',\
        'MD': 'Maryland',\
        'ME': 'Maine',\
        'MI': 'Michigan',\
        'MN': 'Minnesota',\
        'MO': 'Missouri',\
        'MP': 'Northern Mariana Islands',\
        'MS': 'Mississippi',\
        'MT': 'Montana',\
        'NA': 'National',\
        'NC': 'North Carolina',\
        'ND': 'North Dakota',\
        'NE': 'Nebraska',\
        'NH': 'New Hampshire',\
        'NJ': 'New Jersey',\
        'NM': 'New Mexico',\
        'NV': 'Nevada',\
        'NY': 'New York',\
        'OH': 'Ohio',\
        'OK': 'Oklahoma',\
        'OR': 'Oregon',\
        'PA': 'Pennsylvania',\
        'PR': 'Puerto Rico',\
        'RI': 'Rhode Island',\
        'SC': 'South Carolina',\
        'SD': 'South Dakota',\
        'TN': 'Tennessee',\
        'TX': 'Texas',\
        'UT': 'Utah',\
        'VA': 'Virginia',\
        'VI': 'Virgin Islands',\
        'VT': 'Vermont',\
        'WA': 'Washington',\
        'WI': 'Wisconsin',\
        'WV': 'West Virginia',\
        'WY': 'Wyoming'\
                    }
                    
    inv_state = {v: k for k, v in states.items()}
    data = {}
    for key in inv_state.keys():
        avg = 0.0
        for i in range(0,len(USA_add), 1):
            if key in USA_add[i]:
               avg += USA_tweet_scores[i]/len(USA_tweet_scores)
        newkey =  inv_state[key]      
        data[newkey] = round(avg,2)
   # print data
    print "Happiest state is ", max(data, key=data.get)
         
 
if __name__ == '__main__':
    main()

