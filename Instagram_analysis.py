#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pio.templates.default = "plotly_white"

data = pd.read_csv("Instagram data.csv", encoding='latin-1')


# In[2]:


print(data.head())


# In[3]:


print(data.columns)


# In[4]:


print(data.info())


# In[5]:


print(data.describe())


# In[6]:


print(data.isnull().sum())


# In[7]:


fig = px.histogram(data,x='Impressions',nbins=10,title='Distribution of Impressions')
fig.show()


# In[8]:


fig=(px.line(data,x=
            data.index,y='Impressions',title='Impressions over time'))
fig.show()


# In[9]:


fig=go.Figure()
fig.add_trace(go.Scatter(x=data.index,y=data['Likes']))
fig.add_trace(go.Scatter(x=data.index,y=data['Saves']))
fig.add_trace(go.Scatter(x=data.index,y=data['Follows']))


# In[10]:


reach_sources = ['From Home','From Hashtags','From Explore','From Other']
reach_count=[data[source].sum() for source in reach_sources]
colors= ['#FFB6C1', '#87CEFA', '#90EE90', '#FFDAB9']
fig = px.pie(data_frame=data, names=reach_sources, 
             values=reach_count, 
             title='Reach from Different Sources',
             color_discrete_sequence=colors)
fig.show()


# In[11]:


fig = px.scatter(data,x='Profile Visits',y='Follows',trendline='ols',title='Profile visits vs Follows')
fig.show()


# In[12]:


corr_matrix = data.corr()

fig = go.Figure(data=go.Heatmap(z=corr_matrix.values,
                               x=corr_matrix.columns,
                               y=corr_matrix.index,
                               colorscale='RdBu',
                               zmin=-1,
                               zmax=1))

fig.update_layout(title='Correlation Matrix',
                  xaxis_title='Features',
                  yaxis_title='Features')

fig.show()


# In[13]:


all_hashtags = []

for row in data['Hashtags']:
    hashtags = str(row).split()
    hashtags = [tag.strip() for tag in hashtags]
    all_hashtags.extend(hashtags)

hashtag_distribution = pd.Series(all_hashtags).value_counts().reset_index()
hashtag_distribution.columns = ['Hashtag', 'Count']

fig = px.bar(hashtag_distribution, x='Hashtag', 
             y='Count', title='Distribution of Hashtags')
fig.show()


# In[14]:


hashtag_likes = {}
hashtag_impressions = {}

for index, row in data.iterrows():
    hashtags = str(row['Hashtags']).split()
    for hashtag in hashtags:
        hashtag = hashtag.strip()
        if hashtag not in hashtag_likes:
            hashtag_likes[hashtag] = 0
            hashtag_impressions[hashtag] = 0
        hashtag_likes[hashtag] += row['Likes']
        hashtag_impressions[hashtag] += row['Impressions']

likes_distribution = pd.DataFrame(list(hashtag_likes.items()), columns=['Hashtag', 'Likes'])

impressions_distribution = pd.DataFrame(list(hashtag_impressions.items()), columns=['Hashtag', 'Impressions'])

fig_likes = px.bar(likes_distribution, x='Hashtag', y='Likes', 
                   title='Likes Distribution for Each Hashtag')

fig_impressions = px.bar(impressions_distribution, x='Hashtag', 
                         y='Impressions', 
                         title='Impressions Distribution for Each Hashtag')

fig_likes.show()
fig_impressions.show()


# In[ ]:




