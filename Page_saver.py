#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests as req
import glob
import os
import bs4 

def get_article_id(url):
    url = url[::-1]
    skip = 0
    ret = ""
    for i in url:
        if i == '/' and skip == 0:
            skip = 1
        elif i == '/':
            skip = 2
        elif skip == 1:
            ret = i + ret
        elif skip == 2:
            return ret


files = []

fileMode = "w"
directory= "F:/Thesis/Dataset/"
if not os.path.exists(directory):
        os.makedirs(directory)

index="https://www.prothomalo.com/sports/article?page=" 
count = 0

index2="https://www.prothomalo.com"
article_type = "Sports"

i=701
while(i<901):
    url=index+str(i)
    res=req.get(url)
    soup=bs4.BeautifulSoup(res.text,'lxml')
    links=soup.find_all('a',attrs={'class':'link_overlay'})
    i=i+1
    for plink in links:
        link=index2+plink['href']
        count = count + 1
        resp = req.get(link)
        page = resp.text
        article_id = get_article_id(link)
        out_file = open(directory + article_type + '_' +article_id + "_.txt", fileMode, encoding="utf-8")
        out_file.write(page)
        out_file.close()
        print(url+" "+article_id)
    
        
print('Done')
     
        





