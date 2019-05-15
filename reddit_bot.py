import praw
#import config
reddit=praw.Reddit("bot1") #the bot1 is setup in ini file with personal reddit account information
subreddit=reddit.subreddit("learnpython")
print ("load successful!")
for submission in subreddit.hot(limit=5): #print information in terminal
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")
