#!/usr/bin/env python
# coding: utf-8

# # Netflix Stock Analysis Project

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime


# In[5]:


df=pd.read_csv("netflix_stock.csv")


# In[6]:


df


# In[7]:


# for top 5 data 


# In[8]:


df.head()


# In[9]:


sns.set(rc={'figure.figsize':(10,5)})


# In[10]:


# now making date column in the place of index column


# In[11]:


df['Date']=pd.to_datetime(df['Date'])
df=df.set_index('Date')
df.head()


# # Volume of Stock Traded

# In[12]:


sns.lineplot(x=df.index,y=df['Volume'],label="Volume")
plt.title("Volume of Stock versus time")
plt.show()


# # Stock Prices: High,Open and Close

# In[15]:


df.plot(y=['High','Open','Close'],title="Netflix Stock Price")
plt.show()


# # Netflix Stock Price:Day,Month and Year Wise

# In[27]:


fig, (ax1,ax2,ax3)= plt.subplots(3,figsize=(15,10))
df.groupby(df.index.day).mean().plot(y="Volume",ax=ax1,xlabel="Day")
df.groupby(df.index.month).mean().plot(y="Volume",ax=ax2,xlabel="Month")
df.groupby(df.index.year).mean().plot(y="Volume",ax=ax3,xlabel="Year")


# # Top-5 Dates with Highest Stock Price

# In[32]:


a=df.sort_values(by="High",ascending=False).head(5)
a['High']                                    #now here we can see the top 5 dates where the stock price are high


# # Top-5 Dates with Lowest Stock Price

# In[33]:


b=df.sort_values(by="Low",ascending=True).head(5)
b['Low']                            # now here we can see the top 5 dates where the stock prices are low


# Now trying to make the trend for both the high and the low price

# In[40]:


fig,axes=plt.subplots(nrows=1,ncols=2,sharex=True,figsize=(12,5))
fig.suptitle("High and Low Stock per period of time",fontsize=20)
sns.lineplot(ax=axes[0],y=df['High'],x=df.index,color="green")
sns.lineplot(ax=axes[1],y=df['Low'],x=df.index,color="Red")


# In[41]:





# In[ ]:




