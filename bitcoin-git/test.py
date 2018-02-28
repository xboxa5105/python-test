import matplotlib.pyplot as plt
import pandas as pd
import requests
res=requests.get('https://www.coingecko.com/price_charts/1/usd/90_days.json')
data=res.json()
stats=pd.DataFrame(data.get('stats'))
stats.columns=['time','price']
stats.set_index('time',inplace=True)
stats['short']=stats['price'].rolling(window=7,min_periods=1).mean()
stats.plot()
plt.show()