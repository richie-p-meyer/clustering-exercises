#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

import wrangle
import env


# In[2]:


url = env.get_connection('mall_customers')
query = 'select * from customers'
df = pd.read_sql(query,url)


# In[3]:


df.describe()


# In[4]:


df.info()


# In[5]:


df = wrangle.assign_outlier(df,['age','annual_income','spending_score'])


# In[6]:


wrangle.print_outliers(df)


# In[7]:


df = pd.read_sql(query,url) # Remove outlier columns


# In[8]:


train, X_train, y_train, X_val, y_val, X_test, y_test = wrangle.split_data(df,'spending_score')


# In[9]:


# Get dummies for 'gender' for all X sets
X_sets = [X_train,X_val,X_test]
X_new = []

for x in X_sets:
    X_new.append(pd.get_dummies(x,'gender'))

X_train, X_val, X_test = X_new


# In[10]:


X_train,X_val,X_test = wrangle.scale_minmax(X_train,X_val,X_test)


# In[ ]:




