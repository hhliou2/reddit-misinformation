import pandas as pd
import numpy as np
from psaw import PushshiftAPI
import datetime as dt

# Write all post info to disk
def write_dehydrated_data(infotype, infotype_path, before_year, before_day, before_month):
    
    api = PushshiftAPI()
    
    # For each subreddit in list - get 1000 post ID's from before date and save to disk
    start_epoch=dt.datetime(before_year, before_day, before_month).timestamp()
    
    # Keep track of whether to create or append
    first = True
    
    for inf in infotype:
        print(inf)
        for i in range(10):
            print(start_epoch)
            gen = list(api.search_comments(before=int(start_epoch),
                                        subreddit=inf,
                                        filter=['id', 'author'], limit = 10000))
            df = pd.DataFrame([thing.d_ for thing in gen])
            df['subreddit'] = inf

            print(df.shape)
            if len(df) == 0:
                continue
            # Save to either science.csv, myth.csv, or politics.csv
            if first:
                df.to_csv(infotype_path)
                first = False
            # Append to first df
            else:
                df.to_csv(infotype_path, mode = 'a', header = False)

            # Start search from last date
            start_epoch = df['created_utc'].iloc[-1]