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
    df = pd.read_csv(count_dict_path, index_col=0, header=0)
    print(df.head())
    print(df.shape)
    plot = sns.heatmap(df).get_figure()
    plot.savefig(save_path, dpi=400)
#     with open(count_dict_path, 'r') as fp:
#         count_dict = json.load(fp)
        
#     plt.clf()
#     plt.figure(figsize = (15, 14))
#     plt.bar(count_dict.keys(), count_dict.values())
#     plt.xticks(rotation=90)
    
#     plt.savefig(save_path, bbox_inches = 'tight')

def polarity_chart(polarity_dict_path, save_path):
    df = pd.read_csv(polarity_dict_path, index_col = 0, header=0)
    print(df.head())
    print(df.shape)
#     with open(polarity_dict_path, 'r') as fp:
#         polarity_dict = json.load(fp)
        
#     df = pd.DataFrame(polarity_dict).T
#     df.plot(kind='bar')
    
#     plt.savefig(save_path, bbox_inches = 'tight')