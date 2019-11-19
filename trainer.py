#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.model_selection import train_test_split

dataset_url = 'F:/Thesis/X.csv'
data = pd.read_csv(dataset_url)
print(data.head())


# In[2]:


dataset_url2 = 'F:/Thesis/Y.csv'
data2 = pd.read_csv(dataset_url2)
print(data2.head())


# In[6]:


X=data
Y=data2

X_train, X_test, y_train, y_test = train_test_split(X, Y,test_size=0.2)
print("\nX_train:\n")
print(X_train.head()) 
print(X_train.shape)

print("\nX_test:\n")
print(X_test.head())
print(X_test.shape)


# In[10]:


get_ipython().run_cell_magic('time', '', 'from skmultilearn.problem_transform import BinaryRelevance\nfrom sklearn.svm import LinearSVC\nfrom sklearn.metrics import f1_score,precision_score,recall_score,hamming_loss\n\nclassifier = BinaryRelevance(LinearSVC())\nclassifier.fit(X_train,y_train)\npredictions = classifier.predict(X_test)\n\nprint(precision_score(y_test, predictions, average="micro"))\nprint(recall_score(y_test, predictions, average="micro"))\nprint(hamming_loss(y_test, predictions))\nprint(f1_score(y_test, predictions, average="micro"))')


# In[7]:


from sklearn.metrics import f1_score

f1_score(y_test, predictions, average="micro")


# In[ ]:




