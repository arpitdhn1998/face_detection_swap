#!/usr/bin/env python
# coding: utf-8

# In[39]:


import numpy 
import pandas


# In[40]:


db=pandas.read_csv("Salary.csv")
db


# In[41]:


y=db['Salary']


# In[42]:


x=db['Years'].values.reshape(17,1)


# In[43]:


x.shape


# In[44]:


type(x)


# In[45]:


from sklearn.linear_model import LinearRegression


# In[46]:


model=LinearRegression()


# In[47]:


model.fit(x,y)


# In[48]:


model.predict([[2.5]])


# In[50]:


import joblib


# In[51]:


joblib.dump(model,"MLmodel")


# In[ ]:
print(model.predict([[2.5]]))



