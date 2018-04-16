
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


dat1 = pd.Series([1, 3, 5, np.nan, 6, 8])
dat1


# In[3]:


type(dat1)


# In[4]:


dat2 = pd.Series([1, np.nan, 5, np.nan, 6, 8])
dat2


# In[8]:


# 날짜 Data 생성
dates = pd.date_range('20130101', periods =6)
print(dates)


# #### dataframe 만들기

# In[9]:


df = pd.DataFrame(np.random.randn(6,4),
                 index = dates, columns = list("ABCD"))
df


# In[12]:


df2 = pd.DataFrame({'A': 1. , 
                   'B' : pd.Timestamp('20130103'), 
                   'C' : pd.Series(1, index=list(range(4)), dtype= 'float32'),
                   'D' : np.array([3]*4, dtype = 'int32'), 
                   'E' : pd.Categorical(["test", "train", "test", "train"]), 
                   'F' : "foo"})
df2


# In[14]:


type(df2)


# In[16]:


df2 = pd.DataFrame({'Date': dates, 
                   'A' : dat1, 'B': dat2})
df2


# In[29]:


df2.dtypes


# In[30]:


df2.shape


# In[32]:


df2.info()


# In[33]:


df2.index


# In[36]:


df3 = df2.copy()
df3


# In[38]:


# set_index 인덱스 설정
df3_idx = df3.set_index("Date")
df3_idx


# In[40]:


df3_idx.index


# In[42]:


df = pd.DataFrame({'month' : [1, 4, 7, 10, 12], 
                  'year' : [2012, 2014, 2013, 2014, 2015], 
                  'sale' : [55, 40, 84, np.nan, 30]})
df1 = df.set_index('month')
df1


# In[44]:


df2_idx = df.set_index(['year', 'month'])
df2_idx


# In[47]:


df2.columns


# In[51]:


print(df)
df.describe()


# In[52]:


print(df2)
df2.T

