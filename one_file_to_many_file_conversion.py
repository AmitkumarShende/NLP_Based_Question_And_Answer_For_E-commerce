# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 22:04:32 2020

@author: Dell
"""
# Breaking the datafile into four files using "chunk_size=8000" Method
# Import libraries
import pandas as pd
import numpy as np
import os

os.chdir('D:\\Data_science\\Projects\\Excelr_project\\project1_NLP\\Output\\Final1')

#Reading the csv file
df1=pd.read_csv('df1.csv')
df1.dtypes
df1.columns
df1=df1.drop(['questionType', 'asin', 'answerTime', 'unixTime', 'answerType'],  axis = 1)
df1['Q_and_A'] =  df1['question']+ " "+df1['answer']
df1['keywords']=""

df1.to_csv ('df2.csv', index = False, header=True)

chunk_size=80000
batch_no=1
for chunk in pd.read_csv('df2.csv', chunksize=chunk_size):
    chunk.to_csv ('df2_'+str( batch_no) +'.csv', index = False)
    batch_no +=1


