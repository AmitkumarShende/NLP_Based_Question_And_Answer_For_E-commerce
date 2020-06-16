# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 05:06:29 2020

@author: Dell
"""

import json
import csv
import ast
import os
import pandas as pd
import time
import numpy as np

os.chdir('D:\\Data_science\\Projects\\Excelr_project\\project1_NLP\\Output\\april5\\creating_slice')

#Reading the csv file
col_Names=["Q_and_A", "Score"]
df1 = pd.read_csv("recommandation.csv",names=col_Names)
df1=df1.sort_values(by=['Score'], ascending=False)
df1.head(5)

for j in range(5):
    split_lines=''
    split_lines=df1['Q_and_A'].loc[j] 
    print(split_lines.split('\n', 1)[0])
    print(split_lines.split('\n', 1)[1])
    print('\n')
    
    