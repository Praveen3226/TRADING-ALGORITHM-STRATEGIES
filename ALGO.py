#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
plt.style.use("dark_background")


# In[3]:


import pandas as pd
apple = pd.read_csv("APPLE.csv")
apple


# In[5]:


import matplotlib.pyplot as plt
plt.figure(figsize=(12, 5))
plt.plot(apple['Adj Close'], label='Apple')
plt.title('Apple Adj Close Price History')
plt.xlabel("May 27,2014 - Sep 11,2023 ")
plt.ylabel("Adj Close Price USD ($)")
plt.legend(loc="upper left")
plt.show()


# In[6]:


sma30 = pd.DataFrame()
sma30['Adj Close'] = apple['Adj Close'].rolling(window=30).mean()
sma30


# In[7]:


sma100 = pd.DataFrame()
sma100['Adj Close'] = apple['Adj Close'].rolling(window=100).mean()
sma100


# In[8]:


plt.figure(figsize=(18,12))
plt.plot(apple['Adj Close'], label='Apple')
plt.plot(sma30['Adj Close'], label='SMA30')
plt.plot(sma100['Adj Close'], label='SMA100')
plt.title("Apple Adj. Close Price History")
plt.xlabel('May 27,2014 - Sep 11,2023')
plt.ylabel('Adj. Close Price USD($)')
plt.legend(loc='upper left')
plt.show()


# In[9]:


data = pd.DataFrame()
data['apple'] = apple['Adj Close']
data['SMA30'] = sma30['Adj Close']
data['SMA100'] = sma100['Adj Close']
data


# In[10]:


def buySell(data):
  sigPriceBuy = []
  sigPriceSell = []
  flag = -1
  for i in range(len(data)):
    if data ['SMA30'][i] > data['SMA100'][i]:
      if flag != 1:
        sigPriceBuy.append(data['apple'][i])
        sigPriceSell.append(np.nan)
        flag = 1
      else:
        sigPriceBuy.append(np.nan)
        sigPriceSell.append(np.nan)
    elif data['SMA30'][i] < data['SMA100'][i]:
      if flag != 0:
        sigPriceBuy.append(np.nan)
        sigPriceSell.append(data['apple'][i])
        flag = 0
      else:
        sigPriceBuy.append(np.nan)
        sigPriceSell.append(np.nan)
    else:
      sigPriceBuy.append(np.nan)
      sigPriceSell.append(np.nan)
  return(sigPriceBuy, sigPriceSell)


# In[12]:


import numpy as np
buySell = buySell(data)
data['Buy Signal Price'] = buySell[0]
data['Sell Signal Price'] = buySell[1]
# To show the data
data


# In[13]:


plt.style.use('classic')
plt.figure(figsize=(18,5))
plt.plot(data['apple'], label='Apple', alpha=0.50)
plt.plot(data['SMA30'], label='SMA30', alpha=0.50)
plt.plot(data['SMA100'],label='SMA100', alpha=0.50)
plt.scatter(data.index, data['Buy Signal Price'], label ='Buy', marker='^',color='darkgreen')
plt.scatter(data.index, data['Sell Signal Price'],label='Sell', marker='v', color='red')
plt.title('Apple Adj. Close Price History Buy and Sell Signals')
plt.xlabel("May 27,2014 - Sep 11,2023")
plt.ylabel("Adj Close Price USD($)")
plt.legend(loc='upper left')
plt.show()


# In[ ]:




