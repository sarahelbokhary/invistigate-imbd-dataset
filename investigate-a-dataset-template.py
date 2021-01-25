#!/usr/bin/env python
# coding: utf-8

# 
# # Project: analyzing IMDB Dataset
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# </ul>

# <a id='intro'></a>
# ## Introduction
# 
# ### analyzing of any data will give us insights so we could get the most benifits from our investment. so, if we analyze an old data we can get prediction of what features will give us the most revnue. that is what i will do in this notebook. i will search for what revneue depends on the most and who is the most popular actor we could ask him\her to act in the film. 

# In[1]:


# Use this cell to set up import statements for all of the packages that you
#   plan to use.
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
# Remember to include a 'magic word' so that your visualizations are plotted
#   inline with the notebook. See this page for more:
#   http://ipython.readthedocs.io/en/stable/interactive/magics.html


# <a id='wrangling'></a>
# ## Data Wrangling
# 
# 
# 
# ### the data i will use has many defects : 1- there are many features which are not useful to me so i will drop it using drop() function                                                                                                                                                                            2- since the data is relativily large so i can drop the rows which contains misiing values without being affected using .dropna() function
# 
# ### General Properties

# In[2]:


# Load your data and print out a few lines. Perform operations to inspect data
df=pd.read_csv("tmdb-movies.csv")
#   types and look for instances of missing or possibly errant data.
df.head()


# In[3]:


df.shape


# In[4]:


df.describe()


# In[5]:


df.info()


# In[6]:


# After discussing the structure of the data and any problems that need to be
#   cleaned, perform those cleaning steps in the second part of this section.


# In[7]:


df.drop(["id","imdb_id","homepage","tagline","production_companies","keywords","runtime","release_date","budget_adj","revenue_adj"],axis=1,inplace=True)


# In[8]:


df.head()


# In[9]:


df.info()


# In[10]:


df.dropna(inplace=True)


# In[11]:


df.drop_duplicates()


# In[12]:


df.info()


# In[ ]:





# In[ ]:





# <a id='eda'></a>
# ## Exploratory Data Analysis
# 
# 
# 
# ## What kinds of properties are associated with movies that have high revenues?

# In[13]:


# Use this, and more code cells, to explore your data. Don't forget to add
#   Markdown cells to document your observations and findings.
df.corr()


# ## from the above output we can concolude that the revenue depends the most on 3 main features respectively : 
# ### 1- vote_count
# ### 2- budget
# ### 3- popularity

# ### I will visualize the relation between the revenue and those featuers to show the positive correlation between them and make it easier and clearly to understand without looking to the numerical statistics 

# In[23]:


df.plot(kind="scatter",x="vote_count",y="revenue",figsize=(8,4))
plt.title("the relation between the vote counts and the revenue")
plt.xlabel("vote counts")
plt.ylabel("revenue")
plt.show()


# In[22]:


df.plot(kind="scatter",x="budget",y="revenue",figsize=(8,4))
plt.title("the relation between the budget and the revenue")
plt.xlabel("budget")
plt.ylabel("revenue")
plt.show()


# In[21]:


df.plot(kind="scatter",x="popularity",y="revenue",figsize=(8,4))
plt.title("the relation between the popularity and the revenue")
plt.xlabel("popularity")
plt.ylabel("revenue")
plt.show()


# ### so, it's obivious that revenue has a positive correlation with each of the three mentioned features

# ## Who is the most frequent actor?

# In[24]:


# Continue to explore the data to address your additional research
#   questions. Add more headers as needed if you have more questions to
#   investigate.
df["cast"].head()


# In[25]:


actors= df["cast"].str.cat(sep="|")
actor=pd.Series(actors.split('|'))
a=actor.value_counts(ascending=False)
a


# In[26]:


top_10=a.head(10)


# ### I will visualize the results i have got to show the most frequent actor easily 

# In[35]:


top_10.plot(kind="pie",autopct="%.1f%%")


# ## so it's obivious that Robert De Niro is the most frequent actor 

# ### Q3 :Which Genre Has The Highest Release Of Movies ?

# In[28]:


df["genres"].value_counts()


# In[29]:


genre=df["genres"].str.cat(sep="|")
gen=pd.Series(genre.split('|'))
g=gen.value_counts(ascending=False)
g


# In[30]:


top_genres = g.head(10)
top_genres


# ### I will visualize the genres to show the top genre without looking to any statistics

# In[34]:


top_genres.plot(kind="barh")
plt.title("the top 10 genres and their numbers")
plt.xlabel(" their numbers")
plt.ylabel(" the genres")
plt.show()


# <a id='conclusions'></a>
# ## Conclusions
# ### What kinds of properties are associated with movies that have high revenues?
# #### first I have calculated the correlation between the features to know whic featueres that the revnue depends on, then I concluded that it depends mainly on three features which are the vote_count , the budget & the popularity. so i visualize it to make it more clearely to understand without looking to the numbers. so, i have got that all of these featuers correlated positively with the revenue.
# ### Who is the most frequent actor?
# #### at first i noticed that there is no columns for each actor but there is only one column contains the whole cast but mainly i want to know who is the most frequent actor in the data so i needed to separate each actor in the cast i did it using first the (str.cat(sep="|")) method then i used (pd.Series(actors.split('|')) ) so i get each actor separately then i arranged them descendingly so i get the top 10 actors and i picked the first one who was Robert De Niro and i visualize it by "Pie" chart to make it clearely.
# ### Which Genre Has The Highest Release Of Movies ?
# #### i've noticed that there are many films which doesn't have only one genre so i splitted the genres to each genre as i did with the acotors then i arranged them descendingly so i get the top 10 and i concluded that Drama has the highest release of the movies the i visualized it by the "barh" chart to make it clearely.
# 
# ### additional information could be useful to improve analysis :
# #### since we get the most frequent actor and the most popular genre we can study the relation between the revenue and these features so we can get the most benifit
# ### Data 
# #### the data has been very useful to me to do my analysis and get these results although it had many features i didn't need so i dropped it, also it contained missing values and since the dataset won't be affected if i dropped these rows so, idropped them.
# ### References
# #### https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.barh.html
# #### https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.cat.html
# 

# In[ ]:




