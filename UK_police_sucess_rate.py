import sys, os
import pandas as pd 
import seaborn
import matplotlib.pyplot as plt



#scrape data from each file in the 2021-01 folder of police_data file and combine into one csv file
def scrape_data(file):
    path = 'police_data/' + file
    files = os.listdir(path)
    df = pd.DataFrame()
    for file in files:
        df = df.append(pd.read_csv(path + '/' + file, sep=','))
    df.to_csv('police_data_summed.csv', index=False)

#generate list of all files in police_data

def generate_file_list():
    path = 'police_data'
    files = os.listdir(path)
    return files

def all_folders():
    for x in generate_file_list():
        scrape_data(x)

def sucess_rate():
    
    types = ['Unable to prosecute suspect', 'no suspect identified', 'suspect charged', 'suspect charged and convicted', 'Court result unavailable', 'Unable to prosecute suspect']
    police_df_2 = police_df[['Outcome']]

    nan_value = float("NaN")
    police_df_2.replace("", nan_value, inplace=True)
    police_df_2.dropna(how='all', axis=1, inplace=True)

    police_df_2.to_csv('police_df_2.csv', index=False)



def sort_by_race():
    #write code to create a dataframe called race_df the contains the column 'Self-defined ethnicity' and ['Location']
    #create a dataframw called police_d_1 with the columns Self-defined ethnicity and Location from police_df
    police_d_1 = police_df[['Self-defined ethnicity', 'Officer-defined ethnicity', 'Falls within']]
    print(police_d_1.sample(10))

    #save police_d_1 to a csv file
    police_d_1.to_csv('police_d_1.csv', index=False)

police_df = pd.read_csv('police_data_summed.csv', low_memory=False)
sucess_rate()