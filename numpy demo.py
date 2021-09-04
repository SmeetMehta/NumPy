#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
list1=[1,2,3]
np.array(list1)


# In[2]:


list2=[[1,2,3],[4,5,6],[7,8,9]]
np.array(list2)


# In[3]:


np.arange(0,10) # 0 included 10 excluded


# In[4]:


np.arange(0,11,2) # 0 included 11 excluded and at interval of 2


# In[5]:


np.zeros((2,3))


# In[6]:


np.ones((2,3))


# In[7]:


np.linspace(0,5,10)  # starting from 0 to 5 we get 10 evenly spaced points


# In[8]:


np.eye(3)


# In[11]:


arr=np.arange(25)
arr


# In[14]:


arr.reshape(5,5)


# In[16]:


arr.max()


# In[17]:


arr.min()


# In[18]:


arr.argmax()


# In[20]:


arr.argmin()


# In[22]:


arr.shape


# In[ ]:




