import praw
import pdb
import re
import os
import time

reddit=praw.Reddit("bot1")
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to=[]
else:
    with open("posts_replied_to.txt","r") as f:
        posts_replied_to=f.read()
        posts_replied_to=posts_replied_to.split("\n")
        posts_replied_to=list(filter(None, posts_replied_to))

community="pythonforengineers"
subreddit=reddit.subreddit(community)

def run_bot(subreddit):
    for submission in subreddit.comments(limit=2):
        print("Comment: ", submission.body)
        #if submission.id not in posts_replied_to:
        if re.search("i love python", submission.body, re.IGNORECASE):
            submission.reply("Botty bot says: haha, I love python too!")
            print ("Bot replying to:")
            posts_replied_to.append(submission.id)
    with open("posts_replied_to.txt","w") as f:
        for post_id in posts_replied_to:
            f.write(post_id +"\n")
    print ("now sleep for 10 seconds...")
    time.sleep(10)
n=5
while n>0:
    run_bot(subreddit)
    n-=1
