#!/usr/bin/env python
# coding: utf-8

# In[53]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import plotly.express as px


# In[54]:


os.listdir('D:\Anaconda\python_analysis\Covid-19')


# In[55]:


def read_data(path, file_name):
    return pd.read_csv(path + '/' + file_name)


# In[56]:


path = 'D:\Anaconda\python_analysis\Covid-19'
file_name = 'worldometer_data.csv'
world_data = read_data(path, file_name)


# In[57]:


world_data.head()


# In[58]:


day_wise = read_data(path, files[2])


# In[59]:


group_data = read_data(path, files[3])


# In[60]:


usa_data = read_data(path, files[4])


# In[61]:


province_data = read_data(path, files[1])


# In[62]:


province_data.shape


# In[63]:


province_data.head()


# In[64]:


world_data.columns


# In[26]:





# In[65]:


columns = ['TotalCases', 'TotalDeaths', 'TotalRecovered', 'ActiveCases']
for i in columns:
    fig = px.treemap(world_data.iloc[0:20], values = i, path = ['Country/Region'], title = 'Treemap representation of 20 different countries for {}'.format(i))
    fig.show()
    


# In[66]:


day_wise.columns


# In[67]:


px.line(day_wise, x = 'Date', y = [ 'Confirmed', 'Deaths', 'Recovered', 'Active'], title = 'Covid cases', template = 'plotly_dark')


# In[68]:


world_data.head()


# In[71]:


pop_test_ratio = world_data['Population']/world_data['TotalTests'].iloc[0:20]


# In[74]:


fig = px.bar(world_data.iloc[0:20], x ='Country/Region', y = pop_test_ratio[0:20], color = 'Country/Region',title = 'Population to test done ratio')
fig.show()


# In[75]:


world_data.columns


# In[76]:


px.bar(world_data.iloc[0:20], x = 'Country/Region', y = ['Serious,Critical', 'TotalDeaths', 'TotalRecovered', 'ActiveCases', 'TotalTests'])


# In[81]:


fig = px.bar(world_data.iloc[0:10],  y = 'Country/Region', x = 'TotalCases', color='TotalCases', text = 'TotalCases')
fig.update_layout(template='plotly_dark', title_text = 'Top 10 countries of total confirmed cases')
fig.show()


# In[86]:


fig = px.bar(world_data.sort_values(by = 'TotalDeaths', ascending = False)[0:10],  y = 'Country/Region', x = 'TotalDeaths', color='TotalDeaths', text = 'TotalDeaths')
fig.update_layout(template='plotly_dark', title_text = 'Top 10 countries of total deaths cases')
fig.show()


# In[87]:


fig = px.bar(world_data.sort_values(by = 'TotalRecovered', ascending = False)[0:10],  y = 'Country/Region', x = 'TotalRecovered', color='TotalRecovered', text = 'TotalRecovered')
fig.update_layout(template='plotly_dark', title_text = 'Top 10 countries of total recovered cases')
fig.show()


# In[94]:


labels = world_data[0:15]['Country/Region'].values
cases = ['TotalCases', 'TotalDeaths', 'TotalRecovered', 'ActiveCases']
for i in cases:
    fig = px.pie(world_data[0:15],values=i,names=labels,hole=0.3,title = i)
    fig.show()


# In[95]:


deaths_to_confirmed = world_data['TotalDeaths']/world_data['TotalCases']
deaths_to_confirmed


# In[96]:


px.bar(world_data, x = 'Country/Region', y = deaths_to_confirmed, title = 'Deaths to confirmed ratio of worst affected countries')


# In[97]:


deaths_to_recovered = world_data['TotalDeaths']/world_data['TotalRecovered']


# In[98]:


px.bar(world_data, x = 'Country/Region', y = deaths_to_recovered, title = 'Deaths to recovered ratio of worst affected countries')


# In[99]:


world_data['Serious,Critical']/world_data['TotalDeaths']


# In[100]:


px.bar(world_data, x = 'Country/Region', y = world_data['Serious,Critical']/world_data['TotalDeaths'], title = 'Serious to death ratio of worst affected countries')


# In[115]:


from plotly.subplots import make_subplots
import plotly.graph_objects as go


# In[123]:


def country_visualisation(dataframe, country):
    data = dataframe[dataframe['Country/Region'] == country]
    data2 = data.loc[:,['Date', 'Confirmed', 'Deaths', 'Recovered', 'Active']]
    fig = make_subplots(rows = 1, cols = 4, subplot_titles = ('Confirmed', 'Deaths', 'Recovered', 'Active'))
    fig.add_trace(
    go.Scatter(name ='Confirmed',x=data2['Date'],y=data2['Confirmed']),row=1,col=1
    )
    fig.add_trace(
    go.Scatter(name ='Deaths',x=data2['Date'],y=data2['Deaths']),row=1,col=2
    )
    fig.add_trace(
    go.Scatter(name ='Recovered',x = data2['Date'],y=data2['Recovered']), row=1,col=3
    )
    fig.add_trace(
    go.Scatter(name ='Active',x=data2['Date'],y=data2['Active']), row = 1, col = 4
    )
    fig.update_layout(height = 600, width = 1000, title_text = 'Dated vs Recorded Cases of {}'.format(country), template = 'plotly_dark')
    fig.show() 


# In[124]:


country_visualisation(group_data, 'US')


# In[ ]:




