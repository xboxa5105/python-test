
# coding: utf-8

# In[21]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
url='https://rent.591.com.tw/home/search/rsList?is_new_list=1&type=1&kind=0&searchtype=1&region=1&section=3&firstRow={}&totalRows=1708'
houdata=[]
for i in range(0,int(1708/30)+1):
    res=requests.get(url.format(i*30),headers=header)
    jd = res.json()
    df = pd.DataFrame(jd['data']['data'])
    df = df[['id','address','floor','allfloor','layout','area','price','browsenum_all']]
    houdata.append(df)



# In[25]:


houdt=pd.concat(houdata)


# In[26]:


houdt


# In[27]:


houdt['price']=houdt['price'].map(lambda i:int(i.replace(',','')))


# In[37]:


houdt=houdt.drop('layout',1)


# In[38]:


houdt['square_feet'] = df['area'] / 0.3025


# In[39]:


houdt


# In[42]:


houdt.applymap(lambda e:'-' if pd.isnull(e) else e)


# In[44]:


houdt.fillna('-')

