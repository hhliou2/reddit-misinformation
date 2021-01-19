import pandas as pd
import numpy as np
from psaw import PushshiftAPI
import datetime as dt

# Strange bug in psaw - can only get comment id's if count <= 500
# Helper function splits sample size to chunks <= 500
def partition_sample_size(size):
    new_size = size
    counter = 1
    lst = [0]
    while new_size > 500:
        new_size = new_size // 2
        counter *= 2
    if counter == 0:
        return [new_size]
    else:
        for i in range(counter):
            lst.append(new_size)
        last_num = size % new_size
        if last_num != 0:
            lst.append(last_num)
        return np.cumsum(lst)

# Load data from disk, sample, return dataframe
def sample(size, infotype_path):
    api = PushshiftAPI()
    
    sizes = partition_sample_size(size)
    df = pd.read_csv(infotype_path)
    samples = df.sample(size, replace=False)
    subsamp_ids = samples['id'].to_list()
    sub_df = None
    
    for i in range(len(sizes)-1):
        gen = list(api.search_comments(
                            ids = subsamp_ids[sizes[i]:sizes[i+1]],
                            filter=['id', 'author', 'score', 'created_utc']))

        if sub_df is None:
            sub_df = pd.DataFrame([thing.d_ for thing in gen])
        else:
            sub_df = sub_df.append(pd.DataFrame([thing.d_ for thing in gen]), ignore_index = True)
    print(sub_df.head())
    print(sub_df.shape)
