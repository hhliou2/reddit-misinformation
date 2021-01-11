import praw
import pandas as pd
import numpy as np
import json

# Load API
def load_api(api_keys):
    with open(api_keys) as f:
        api_keys = json.load(f)
    reddit = praw.Reddit(
        client_id=api_keys['client_id'],
        client_secret=api_keys['client_secret'],
        password=api_keys['password'],
        user_agent=api_keys['user_agent'],
        username=api_keys['username']
    )
    
    return reddit

# Given a dataframe of post ID's, "rehydrate" with relevant information about the author, score, upvote ratio, and num comments
def post_info(submissions):
    submissions['author'] = submissions[0].apply(lambda x: x.author)
    submissions['score'] = submissions[0].apply(lambda x: x.score)
    submissions['upvote_ratio'] = submissions[0].apply(lambda x: x.upvote_ratio)
    submissions['num_comments'] = submissions[0].apply(lambda x: x.num_comments)
    return submissions

# Write all post info to disk
def write_data(infotype, infotype_path, api_keys):
    # Get API
    reddit = load_api(api_keys)
    
    # First subreddit in list - get 1000 top hot posts, rehydrate, and save to disk
    temp = pd.DataFrame(list(reddit.subreddit(infotype[0]).hot(limit=1000)))
    post_info(temp)
    
    # Tell us which subreddit we uploaded
    print(infotype[0])

    # Save to either science.csv, myth.csv, or politics.csv
    temp.to_csv(infotype_path)
    
    # Do for rest of files (appended this time)
    for i in infotype[1:]:
        temp = pd.DataFrame(list(reddit.subreddit(i).hot(limit=1000)))
        post_info(temp)
        print(i)

        temp.to_csv(infotype_path, mode = 'a', header = False)