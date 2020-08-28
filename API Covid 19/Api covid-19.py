#!/usr/bin/env python
# coding: utf-8

# # API Covid-19 

# In[7]:


import json
import requests

import pandas as pd
import seaborn as sns


# In[8]:


url = "https://covid19-brazil-api.now.sh/api/report/v1" 

headers = {
    'x-rapidapi-host': "covid19-brazil-api.now.sh/api/report/v1",
    'x-rapidapi-key': "9df309daf7msh4afaa54184a9cc4p1801d1jsn0feb78294818"
    }

response = requests.request("GET", url, headers=headers)
print(response)


# In[9]:


parsed_data = json.loads(response.text)
print(parsed_data)


# In[10]:


parsed_data


# In[11]:


def flatten_json(json):
    dict1 = {}
    
    def flatten(i, name=""):
        if type(i) is dict:
            for a in i:
                flatten(i[a], name + a + '_')
        else:
            dict1[name[:-1]] = i
    
    flatten(json)
    return dict1


# In[12]:


#Data Frame

dados = pd.DataFrame.from_dict(flatten_json(parsed_data),orient="index")
dados


# In[ ]:




