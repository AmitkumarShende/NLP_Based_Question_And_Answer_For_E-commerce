# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 22:04:32 2020

@author: Dell
"""
# Import libraries
import pandas as pd
import numpy as np
import os
import re
import operator
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import string
words = set(nltk.corpus.words.words())

os.chdir('D:\\Data_science\\Projects\\Excelr_project\\project1_NLP\\Output\\Final1')
#============================================
#Reading the csv file
# change the reading file name to df2_1 to df2_2 and on...to df2_4
df=pd.read_csv('df2_4.csv')
df1=df.copy()
df1.dtypes
df1.isnull().sum()
length=len(df1['Q_and_A'])

    for j in range(len(df1['Q_and_A'])):    
    #def pre_process(text):  
        i=0  
        text=''
        text=df1['Q_and_A'].loc[j] 
        text = re.sub(r"http\S+", "", text) 
        text = text.replace('.',' ') 
        text=re.sub("<!--?.*?-->","",text)
        text=re.sub("(\\d|\\W)+"," ",text)
        text = re.sub(r'\s+',' ',re.sub(r'[^\w \s]','',text) ).lower() 
        text=text.split()
        text=" ".join(sorted(set(text), key=text.index))
        if len(text) == 0:
            text='It is not having any subject'
        sentences = nltk.sent_tokenize(text)
        lemmatizer = WordNetLemmatizer()  
        for i in range(len(sentences)):
            words1 = nltk.word_tokenize(sentences[i])
            words1 = [lemmatizer.lemmatize(word) for word in words1 if word not in set(stopwords.words('english'))]
            sentences[i] = ' '.join(words1)
        if len(sentences[i]) == 0:
            sentences[i]='subject unavailble'
        df1['keywords'].loc[j]=sentences[i]
      
    # remove the lines which don't have keywords after cleaning the data
    df1 = df1[~df1['keywords'].isin(['subject unavailble'])]
    df1 = df1[df1['keywords'].notna()]
    df1=df1.drop(['Q_and_A'],  axis = 1)
    df1['Q_and_A'] = 'Question:' + df1['question'] + '\n' +'Answer  :'+df1['answer']
   
    # change the saving file name to df3_1 to df3_2 and on... to df3_4
    
   # df1.to_csv ('df3_'+str(k) +'.csv', index = False, header=True) 
    df1.to_csv ('df3_4.csv', index = False, header=True) 

