import sys, os
import pandas as pd 
import seaborn
import matplotlib.pyplot as plt

#create a graph of the centers of religious population
df = pd.read_csv('TS031-2021-1.csv', sep=',')
for x in range(1, 7):
    religion = ['Christian', 'Buddhist', 'Hindu', 'Jewish', 'Muslim', 'Sikh']
    graph = df[df['Religion (detailed) (58 categories) Code'] == x].sort_values(by='Observation').tail(20).plot.bar(x='Lower Tier Local Authorities', y='Observation')
    graph.figure.savefig(religion[x - 1] + '.png', bbox_inches='tight')

police_df = pd.read_csv('police_data_summed.csv', low_memory=False)

def crime_vs_percent_religion():
    return