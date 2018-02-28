import matplotlib.pyplot as plt
import pandas as pd
import requests
import xlwt
res=requests.get('https://www.coingecko.com/price_charts/1/usd/90_days.json')
data=res.json()
stats=pd.DataFrame(data.get('stats'))
stats.columns=['time','price']
stats.set_index('time',inplace=True)
file1=stats.head(100)
file2=stats.describe()
file1.to_csv('比特幣分析.csv')
file2.to_csv('比特幣分析1.csv')
stats.plot()
plt.show()