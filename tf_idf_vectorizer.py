#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import glob
import math
import operator
import csv
files=[]
        
input_path= "F:/Thesis/Dataset_tokenized/"
inp="F:/Thesis/tfidf.txt"
os.chdir(input_path)


for file_ in glob.glob("*"):
    files.append(file_)
    
os.chdir('..')

doc_count={}

superList=[]



fields=[]

filename = "F:/Thesis/university_records.csv"


i=0

doc = open(inp, encoding="utf-8").readlines()
for line in doc:
    tokens = line.replace("\n","").split(",")
    key = tokens[0]
    if(i<30000):
        if key not in fields:
            fields.append(key)
            i=i+1

            
superList.append(fields)
            


for file_ in files:
    doc = open(input_path+file_, encoding="utf-8").readlines()
    for line in doc:
        tokens = line.replace("\n","").split(",")
        key = tokens[0]
        value = int(tokens[1])
        if key not in doc_count.keys():
            doc_count[key] = 1
        else:
            doc_count[key] = doc_count[key]+1

for file_ in files:
    doc = open(input_path+file_, encoding="utf-8").readlines()
    freq_count={}
    word_count=0
    tfidf=[]
    for line in doc:
        tokens = line.replace("\n","").split(",")
        key = tokens[0]
        value = int(tokens[1])
        
        if key not in freq_count.keys():
            freq_count[key] = 1
        else:
            freq_count[key] = freq_count[key]+value
        word_count= word_count+value
    summ=0.0
    for field in fields:
        if field not in freq_count.keys():
            tf=0
        else:
            tf = freq_count[field]/word_count
        idf=math.log(len(files)/doc_count[field])
        tfidf.append(tf*idf)
        summ=summ+(tf*idf)
        
    
    if(summ==0.0):
        print(file_)
    superList.append(tfidf)
    
    
with open(filename, 'w',encoding="utf-8") as csvfile: 
     #creating a csv writer object 
    csvwriter = csv.writer(csvfile, lineterminator = '\n') 
      
    #writing the fields 
    csvwriter.writerows(superList) 
    
print("Done")
        
        


    

