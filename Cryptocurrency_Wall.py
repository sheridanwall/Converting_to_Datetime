#!/usr/bin/env python
# coding: utf-8

# # Cryptocurrency prices
# 
# * **Filename:**  `cryptocurrencies.csv`
# * **Description:** Cryptocurrency prices for a handful of coins over time.
# * **Source:** https://coinmarketcap.com/all/views/all/ but from a million years ago (I cut and pasted, honestly)
# 
# ### Make a chart of bitcoin's high, on a weekly basis
# 
# You might want to do the cherry blossoms homework first, or at least read the part about `format=` and `pd.to_datetime`.
# 
# *Yes, that's the entire assignment. It isn't an exciting dataset, but it's just dirty enough to make charting this a useful experience.*

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv("cryptocurrencies.csv")


# In[3]:


df.head()


# In[20]:


df['datetime'] = pd.to_datetime(df["date"], format="%d-%b-%y")


# In[21]:


df.head()


# In[23]:


df.datetime.dt.day


# In[28]:


df.resample('W', on='datetime').high.sum()


# In[33]:


df.dtypes


# In[34]:


df['high'] = df.high.str.replace(',','')


# In[37]:


df['high'] = df.high.astype(float)


# In[38]:


df.resample('W', on='datetime').high.sum()


# In[40]:


df.resample('W', on='datetime').high.sum().plot()

