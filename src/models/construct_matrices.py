import pandas as pd
import numpy as np
import os

def users_by_subreddit(sci_path, poli_path, myth_path):
    paths = [sci_path, poli_path, myth_path]
    users_by_sub = dict()
    
    for data_path in paths:
        df = pd.read_csv(data_path)
        for sub in df['subreddit'].unique():
            users_by_sub[sub] = df['author'].loc[df['subreddit'] == sub]
    return users_by_sub

def shared_users(users_by_sub):
    cross_counts = dict()
    for keys1, values1 in users_by_sub.items():
        for keys2, values2 in users_by_sub.items():
            cross_counts[keys1 + ', ' + keys2] = pd.Series(list(set(values1).intersection(set(values2))))
    return cross_counts

def count_matrix(shared_users):
    matrix_counts = dict()
    for keys, values in shared_users.items():
        matrix_counts[keys] = len(values)
    return matrix_counts

def polarity_matrix(shared_users, polarity_path):
    matrix_polarities = dict()
    polarities = pd.read_csv(polarity_path)
    
    for keys, values in shared_users.items():
        df = pd.DataFrame(values).merge(polarities, how='left', left_on=0, right_on='Unnamed: 0')
        avg_science = df['science (%)'].mean()
        avg_myth = df['myth (%)'].mean()
        avg_politics = df['politics (%)'].mean()
        matrix_polarities[keys] = [avg_science, avg_myth, avg_politics]

    return matrix_polarities
