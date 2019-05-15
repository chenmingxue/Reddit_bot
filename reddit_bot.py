import praw
#import config
reddit=praw.Reddit("bot1")
subreddit=reddit.subreddit("learnpython")
print ("load successful!")
for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")
