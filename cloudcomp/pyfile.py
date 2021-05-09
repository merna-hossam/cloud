#!/usr/bin/env python
# coding: utf-8

# In[1]:


beyond = open('lovecraft.txt', 'r', errors = 'ignore')


# In[2]:


beyond = beyond.read()


# In[3]:


beyond.strip('\n')


# In[4]:


pride = open('austine.txt', 'r', errors = 'ignore')


# In[5]:


pride = pride.read()


# In[6]:


pride.strip()


# In[7]:


beyond=beyond.lower().split()
pride=pride.lower().split()


# In[8]:


intersection= set(beyond) & set(pride)


# In[9]:


intersection


# In[10]:


print(len(intersection))


# In[14]:


import nltk


# In[11]:


print(intersection)


# In[15]:


nltk.download('stopwords')


# In[16]:


from nltk.corpus import stopwords


# In[17]:


stop_words1 = set(stopwords.words('english'))


# In[18]:


beyond = [w for w in beyond if not w in stop_words1 and w.isalpha()]


# In[19]:


intersection= set(beyond) & set(pride)


# In[20]:


print(len(intersection))


# In[22]:


import string


# In[23]:


print(intersection)


# In[24]:


table1 = str.maketrans('', '', string.punctuation)


# In[25]:


beyond=[w.translate(table1)for w in beyond]


# In[26]:


beyond =[word.lower()for word in beyond]


# In[27]:


table2 = str.maketrans('', '', string.punctuation)


# In[28]:


pride = [w.translate(table2)for w in pride]


# In[29]:


pride =[word.lower()for word in pride]


# In[30]:


intersection= set(beyond) & set(pride)


# In[31]:


print(len(intersection))


# In[32]:


stop_words2 = set(stopwords.words('english'))


# In[33]:


pride = [w for w in pride if not w in stop_words2 and w.isalpha()]


# In[34]:


intersection= set(beyond) & set(pride)


# In[35]:


print(len(intersection))


# In[36]:


intersection


# In[37]:


print(intersection)


# In[ ]:




