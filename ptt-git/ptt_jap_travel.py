
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
ptt_jp=[]
url1 = 'https://www.ptt.cc/bbs/Japan_Travel/index{}.html'
for i in range(5693,5642,-1):
    res = requests.get(url1.format(i))
    soup = BeautifulSoup(res.text, 'lxml')
    articles = soup.find_all('div', 'r-ent')
    for article in articles:
        
        NOT_EXIST = BeautifulSoup('<a>本文已被刪除</a>', 'lxml').a        
        meta = article.find('div', 'title').find('a') or NOT_EXIST
        title = meta.getText().strip()
        link = meta.get('href')
        date = article.find('div', 'date').getText()
        author = article.find('div', 'author').getText()
        ptt_jp.append({'title':title, 'date':date, 'author':author})
        


# In[5]:


ptt_jap=pd.DataFrame(ptt_jp)
ptt_jap=ptt_jap[~ptt_jap['title'].str.contains("被刪除")]
ptt_jap


# In[6]:


ptt_jap.to_csv('ptt_jap_travel.csv',encoding='utf-8-sig')


# In[7]:


ptt_jap[ptt_jap['title'].str.contains("大阪")]


# In[20]:


ptt_japloc={u"東京":len(ptt_jap[ptt_jap['title'].str.contains(u"東京")]),            u"大阪":len(ptt_jap[ptt_jap['title'].str.contains(u"大阪")]),            u"札幌":len(ptt_jap[ptt_jap['title'].str.contains(u"札幌")]),            u"沖繩":len(ptt_jap[ptt_jap['title'].str.contains(u"沖繩")]),            u"京都":len(ptt_jap[ptt_jap['title'].str.contains(u"京都")]),            u"福岡":len(ptt_jap[ptt_jap['title'].str.contains(u"福岡")]),            u"奈良":len(ptt_jap[ptt_jap['title'].str.contains(u"奈良")]),            u"名古屋":len(ptt_jap[ptt_jap['title'].str.contains(u"名古屋")]),            u"輕井澤":len(ptt_jap[ptt_jap['title'].str.contains(u"輕井澤")]),            u"神戶":len(ptt_jap[ptt_jap['title'].str.contains(u"神戶")])}
ptt_japloc


# In[21]:


ptt_japlocdf=pd.DataFrame([ptt_japloc])
ptt_japlocdf


# In[22]:


import matplotlib.pyplot as plt
ptt_japlocdf.plot(kind = 'bar')
plt.show()

