import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import json

def polarity_histogram(polarity_path, save_path):
    plt.clf()
    plt.figure(figsize=(15, 14))
    
    df = pd.read_csv(polarity_path)
    categories = ['science (%)', 'myth (%)', 'politics (%)']
    for c in categories:
        df[c].hist()
        plt.savefig(save_path + '/' + c + '.png', bbox_inches = 'tight')
        plt.clf()
    
def count_chart(count_dict_path, save_path):
    plt.clf()
    
    df = pd.read_csv(count_dict_path, index_col=0, header=0)
    plot = sns.heatmap(df).get_figure()
    plot.savefig(save_path, dpi=400)

def polarity_chart(polarity_dict_path, save_paths):
    plt.clf()
    
    df = pd.read_csv(polarity_dict_path, index_col = 0, header=0)
    
    sub_dfs = [df.copy(), df.copy(), df.copy()]
    for i in range(3):
        for column in sub_dfs[i]:
            sub_dfs[i][column] = df[column].map(lambda x: eval(x)[i])
    
    i = 0
    for s in sub_dfs:
        plot = sns.heatmap(s).get_figure()
        plot.savefig(save_paths[i], dpi=400)
        i += 1
        plt.clf()