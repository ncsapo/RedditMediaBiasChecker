import praw

source = 'Conservative'
destination = 'MediaBiasDebug'

userAgent = 'Media Bias Checker'

cID = '1KM-9tu6se1mcQ'

cSC= 'N_HINlXdwxnk5St6fu6yj_QU6RezLA'

userN = 'MediaBiasChecker_Bot'

userP ='2eH4F_H%PfE_S_7'

numFound = 0

reddit = praw.Reddit(user_agent=userAgent, client_id=cID, client_secret=cSC, username=userN, password=userP)

for submission in reddit.subreddit(source).stream.submissions():
    if not submission.is_self:
        reddit.subreddit(destination).submit(submission.title, url=submission.url)