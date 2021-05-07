#!/usr/bin/python
import praw
import sys
import nwebscraper
import re

import sys
if (sys.version_info>=(3, 0, 0,)):
    from urllib.parse import urlparse, urlencode, parse_qs, urlunparse
else:
    from urlparse import urlparse, parse_qs, urlunparse
    from urllib import urlencode
#Enter your correct Reddit information into the variable below

userAgent = 'Media Bias Checker'

cID = '1KM-9tu6se1mcQ'

cSC= 'N_HINlXdwxnk5St6fu6yj_QU6RezLA'

userN = 'MediaBiasChecker_Bot'

userP ='2eH4F_H%PfE_S_7'

numFound = 0

reddit = praw.Reddit(user_agent=userAgent, client_id=cID, client_secret=cSC, username=userN, password=userP)

subreddit = reddit.subreddit('MediaBiasDebug') #any subreddit you want to monitor

keywords = {'test','test2'} #makes a set of keywords to find in subreddits

for submission in subreddit.hot(limit=10): #this views the top 10 posts in that subbreddit

    n_title = submission.title.lower() #makes the post title lowercase so we can compare our keywords with it.

    for i in keywords: #goes through our keywords

        if i in n_title: #if one of our keywords matches a title in the top 10 of the subreddit

            numFound = numFound + 1
            
            ParsedURL = list(urlparse(submission.url))
            
            URLShort = ParsedURL[1]
            
            try:
                substring = re.search('qwerty(.+?)qwerty', URLShort.replace('.','qwerty')).group(1)
            except AttributeError:
                # AAA, ZZZ not found in the original string
                substring = 'N/A' # apply your error handling
            
            SourceBias = nwebscraper.getBias(substring)[0]
            
            SourceFactual = nwebscraper.getBias(substring)[1]

            print('Bot replying to: ') #replies and outputs to the command line

            print("Title: ", submission.title)

            print("Text: ", submission.selftext)

            print("Score: ", submission.score)
            
            print("Substring: ", substring)
            
            print("Bias: ", SourceBias)

            print("URL: ", URLShort)

            print("---------------------------------")
            
            bot_phrase = URLShort + ' is rated by MediaBiasFactCheck.com to have a ' + SourceBias + ' leaning bias, and a factual reporting rating of: ' + SourceFactual + '. To see how this source was rated, please visit mediabiasfactcheck.com/' + substring + '/'

            print('Bot saying: ', bot_phrase)

            print()

            submission.reply(bot_phrase)

if numFound == 0:

    print()

    print("Sorry, didn't find any posts with those keywords, try again!")