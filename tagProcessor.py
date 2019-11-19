#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import glob
import math
import operator
import csv
import codecs
from bs4 import BeautifulSoup

files=[]
        
input_path= "F:/Thesis/tags2/"
os.chdir(input_path)


for file_ in glob.glob("*"):
    files.append(file_)
    
os.chdir('..')

doc_count={}
freq_count={}
word_count=0

out_file = open('tagNumbers.txt', 'w', encoding="utf-8")


for file_ in files:
    doc = open(input_path+file_, encoding="utf-8").readlines()
    for line in doc:
        tokens = line.replace("\n","")
        if (tokens==""):
            continue
        key = tokens
        
       
        if key not in doc_count.keys():
            doc_count[key] = 1
        else:
            doc_count[key] = doc_count[key]+1
        
       

        
        



iidf={}
for key in doc_count.keys():
    
    idf=doc_count[key]
    iidf[key]=idf

sorted_idf= sorted(iidf.items(),reverse=True, key=operator.itemgetter(1))	

cnt=0;

for item in sorted_idf:
    if(item[1]>=3):
        cnt=cnt+1
    out_file.write(item[0]+","+str(item[1])+"\n")
out_file.close()
print(len(sorted_idf))
print(cnt)


# In[17]:


upor=[]

tgs=[]
t=1
for item in sorted_idf:
    if(t<=96):
        tgs.append(item[0])
        t=t+1
        

upor.append(tgs)
 
    


# In[18]:


import os
import glob
import codecs
from bs4 import BeautifulSoup
import operator

# Returns words from a text
def get_vector(text):
    ret = ""
    stp=["!", "@",'–', "#", "|", "%", "(", ")", "।", "—", ".", "-", "", ",", "’", "•", "‘", ":", "*", "?",
          "০", "১", "২", "৩", "৪", "৫", "৬", "৭", "৮", "৯","অতএব","অথচ","অথবা","অনুযায়ী","অনেক","অনেকে","অনেকেই",
        "অন্তত","অন্য","অবধি","অবশ্য","অর্থাৎ","আই","আগামী","আগে","আগেই","আছে","আজ","আদ্যভাগে","আপনার","আপনি","আবার",
        "আমরা","আমাকে","আমাদের","আমার","আমি","আর","আরও","ই","ইত্যাদি","ইহা","উচিৎ","উত্তর","উনি","উপর","উপরে","এ",
         "এঁরা","এই","একই","একটি","একবার","একে","এক","এখন","এখনও","এখানে","এখানেই","এটা","এটাই","এটি","এত","এতটাই","এতে",
         "এদের","এবং","এবার","এমন","এমনকী","এমনি","এর","এরা","এল","এস","এসে","ঐ","ও","ওদের","ওর","ওরা","ওই","ওকে",
         "ওখানে","ওদের","ওর","ওরা","কখনও","কত","কবে","কয়েক","কয়েকটি","করছে","করছেন","করতে","করবে","করবেন","করলে",
         "করলেন","করা","করাই","করায়","করার","করি","করিতে","করিয়া","করিয়ে","করে","করেই","করেছিলেন","করেছে","করেছেন","করেন",
         "কাউকে","কাছ","কাছে","কাজ","কাজে","কারও","কারণ","কি","কিংবা","কিছু","কিছুই","কিন্তু","কী","কে","কেউ","কেউই","কেখা",
         "কেন","কোটি","কোন","কোনও","কোনো","ক্ষেত্রে","কয়েক","খুব","গিয়ে","গিয়েছে","গিয়ে","গুলি","গেছে","গেল","গেলে","গোটা",
         "চলে","চান","চায়","চার","চালু","চেয়ে","চেষ্টা","ছাড়া","ছাড়াও","ছিল","ছিলেন","জন","জনকে","জনের","জন্য","জানতে","জানা",
         "জানানো","জানায়","জানিয়ে","জানিয়েছে","যে","টি","ঠিক","তখন","তত","তথা","তবু","তবে","তা","তাই","তাও","তাকে","তাতে",
         "তাদের","তার","তারপর","তারা","তারৈ","তাহলে","তিনি","তিনিও","তুমি","তুলে","তেমন","তো","তোমার","থাকবে","থাকবেন","থাকা",
         "থাকায়","থাকে","থাকেন","থেকে","থেকেই","থেকেও","দিকে","দিতে","দিন","দিয়ে","দিয়েছে","দিয়েছেন","দিলেন","দু","দুই","দুটি",
         "দুটো","দেওয়া","দেওয়ার","দেওয়া","দেখতে","দেখা","দেখে","দেন","দেয়","দ্বারা","ধরা","ধরে","ধামার","নয়","না","নাই","নাকি",
         "নাগাদ","নানা","নিজে","নিজেই","নিজেদের","নিজের","নিতে","নিয়ে","নিয়ে","নেই","নেওয়া","নেওয়ার","নেওয়া","নয়","পক্ষে","পর",
         "পরে","পরেই","পরেও","পর্যন্ত","পাওয়া","পাচ","পারি","পারে","পারেন","পেয়ে","প্রতি","প্রথম","প্রভৃতি","পর্যন্ত","প্রাথমিক","প্রায়",
         "ফলে","ফিরে","ফের","বক্তব্য","বদলে","বরং","বলতে","বলল","বললেন","বলা","বলে","বলেছেন","বলেন","বসে","বহু","বা","বাদে",
         "বার","বিনা","বিভিন্ন","বিশেষ","বিষয়টি","বেশ","বেশি","ব্যবহার","ব্যাপারে","ভাবে","ভাবেই","মতো","মতোই","মধ্যভাগে","মধ্যে",
         "মধ্যেই","মধ্যেও","মনে","মাত্র","মাধ্যমে","মোট","মোটেই","যখন","যত","যতটা","যথেষ্ট","যদি","যদিও","যা","যার","যাওয়া","যাওয়ার",
         "যাওয়া","যাকে","যাচ্ছে","যাতে","যাদের","যান","যাবে","যায়","যারা","যিনি","যে","যেখানে","যেতে","যেন","যেমন","রকম","রয়েছে",
         "রাখা","রেখে","লক্ষ","শুধু","শুরু","সঙ্গে","সঙ্গেও","সব","সবার","সমস্ত","সম্প্রতি","সহ","সহিত","সাধারণ","সামনে","সুতরাং","সে",
         "সেই","সেখান","সেখানে","সেটা","সেটাই","সেটাও","সেটি","স্পষ্ট","স্বয়ং","হওয়া","হওয়ায়","হওয়ার","হচ্ছে","হত","হতে","হতেই","হন",
         "হবে","হবেন","হয়","হয়তো","হয়নি","হয়ে","হয়েই","হয়েছিল","হয়েছে","হয়েছেন","হল","হলে","হলেই","হলেও","হলো","হাজার",
         "হিসাবে","হৈলে","হোক","হয়"]
    for x in text:
        ret = ret + x
        
    ret = ret.replace("  ", " ")
    ret = ret.replace("  ", " ")
    ret = ret.split()
    return ret
    
files=[]

output_path= "F:/Thesis/Dataset_tokenized/"
if not os.path.exists(output_path):
        os.makedirs(output_path)
        
output_path2= "F:/Thesis/tags2/"
if not os.path.exists(output_path2):
        os.makedirs(output_path2)
        
input_path= "F:/Thesis/Dataset/"
os.chdir(input_path)

arek="F:/Thesis/stemmed/"


for file_ in glob.glob("*"):
    files.append(file_)
    
os.chdir('..')

labels=[]

i=0

print(len(files))

hua=0


for file_ in files:
    a=[]
    sum=0
    
    page = open(input_path+file_, encoding="utf-8").read()
    soup = BeautifulSoup(page, 'html.parser')
    name_box = soup.find('div', attrs={'class': 'topic_list'})
    
    if name_box is None:
        print("h "+file_)
        hua=hua+1
        #os.remove(input_path+file_)
        #os.remove(arek+file_)
        continue
    
    vec = get_vector(name_box.text)
    for tg in tgs:
        if(tg in name_box.text.split("\n")):
            a.append(1)
            sum=sum+1
        else:
            a.append(0)
    
    upor.append(a)
    if(sum==0):
        print(file_)
        print(i+1)
        hua=hua+1
       # os.remove(input_path+file_)
        #os.remove(arek+file_)
    i=i+1

print(i)
print(hua)
    
   
    
        

    
    
    
    


# In[19]:


import csv
    


# In[20]:


filename = "F:/Thesis/Y.csv"

with open(filename, 'w',encoding="utf-8") as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile, lineterminator = '\n') 
      
    # writing the fields 
    csvwriter.writerows(upor) 
    
print("Done")


# In[ ]:




