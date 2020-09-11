#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
data = pd.read_csv("dset2.csv")


# In[9]:


#data


# In[10]:


#df = data.drop('Essay', axis=1, inplace=True)
#df = data.drop('SMILES-Adenot', axis=1, inplace=True)
#df = data.drop('SMILES', axis=1, inplace=True)
#df = data.drop('SMILES-B', axis=1, inplace=True)
#df = data.drop('Name', axis=1, inplace=True)


# In[11]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
data = pd.read_csv("dset1.csv")
X = data.iloc[:,0:20]
corrmat = data.corr()
top_corr_features = corrmat.index
plt.figure(figsize=(20,20))

#plot heatmap
g=sns.heatmap(data[top_corr_features].corr(),annot=True,cmap="RdYlGn")


# In[12]:


cor_target = abs(corrmat["score"])
relevant_features = cor_target[cor_target>0.3]
relevant_features


# In[ ]:





# In[ ]:





# In[ ]:




