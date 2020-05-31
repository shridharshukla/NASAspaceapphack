#!/usr/bin/env python
# coding: utf-8

# # Introduction :
#                This assignment is part of NASA Spaceapp challenge for Covid19 solutions, May 2020.
#                We are trying to analyze the human factors and different trends in order to predict the hotspots of Covid19.
#                
#                Data Sources and references - 
#                  . space agency data
#                  . European Centre for Disease Prevention and Control
#                  . WHO
#                  . Data world  etc.

# In[49]:


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


# In[2]:


df1 = pd.read_excel('COVID-19-geographic-disbtribution-worldwide-2020-05-29.xlsx')


# Source of this data is European Centre for Disease Prevention and Control.

# In[3]:


df1.head()


# In[8]:


df1.info()


# In[5]:


df1.describe()


# In[4]:


df1.shape


# In[5]:


df1.columns


# In[23]:


df1.isnull().sum()


# In[6]:


print(round(100*(df1.isnull().sum())/len(df1.index)), 2)


# In[7]:


max(round(100*(df1.isnull().sum()/len(df1.index)), 2))


# it shows as Clean data, but still we have few attributes with about 1.4% of missing values

# In[33]:


len(df1[df1.isnull().sum(axis=1) >1].index)


# In[28]:


len(df1[df1.isnull().sum(axis=1) >2].index)


# In[30]:


df1.shape


# We try to vidualize the missing values.

# In[9]:


import matplotlib.pyplot as plt
NanCol = df1.isnull().sum()
plt.figure(figsize=(20,8))
NanCol.plot(kind='bar')
plt.title('Attributes with Na values')
plt.show()


# In[10]:


#As we see that there are 3 attributes with some missing data. we try to view the actual value of it.
df1[['geoId','countryterritoryCode','popData2018']].head(10)


# In[11]:


df1.shape


# In[12]:


df1 = df1.dropna(axis=1, how='all')


# In[13]:


df1.shape


# In[14]:


print(round(100*(df1.isnull().sum())/len(df1.index)), 2)


# In[15]:


df1 = df1.dropna()


# In[16]:


df1.shape


# In[17]:


print(round(100*(df1.isnull().sum())/len(df1.index)), 2)


# Now data has no missing values

# In[ ]:





# As we see the geoId is 2 char code for the counytry which we will replace the missing geoId's with a value as 'NO'. <br/>
# Another we see the countryterritoryCode which in 3 char code for the country, these missing we will replace with 'UNW' as unknown.<br />
# Third attribute we see with missing values is popData2018, this we can impute with 0 as it is a numeric data. 

# In[46]:


#df1.loc[pd.isnull(df1['geoId'])] = 'NO'


# In[47]:


#df1.loc[pd.isnull(df1['countryterritoryCode'])] = 'UNW'


# In[48]:


#df1.loc[pd.isnull(df1['popData2018'])] = 0


# Now we will try to visualize for any missing values.

# In[18]:


import matplotlib.pyplot as plt
NanCol = df1.isnull().sum()
plt.figure(figsize=(20,8))
NanCol.plot(kind='bar')
plt.title('Attributes with Na values')
plt.show()


# As we see, there are no missing values now and our data is fully optimized.

# In[50]:


print(round(100*(df1.isnull().sum())/len(df1.index)), 2)


# No missing values now.

# In[19]:


df1.head()


# In[ ]:





# In[37]:


import matplotlib.pyplot as plt

d = {'Country Population' : df1['popData2018'],
     'No. of CoVid cases' : df1['cases'],
     'No. of casualities' : df1['deaths']}

df_plot = pd.DataFrame(d)

#plt.figure(figsize=(120,20))
df_plot.plot(x='Country Population',y=['No. of CoVid cases','No. of casualities'], figsize=(15,7))

plt.title('CoVid Cases&casualiities Vs  Country Population')

plt.show()


# This shown us that the World's most affected countries are not with most population but with less population as well mostly.
# Hence we can alarm the less populous countries with certain extra measures.

# In[38]:


df_plot.plot(x='Country Population',y=['No. of CoVid cases','No. of casualities'], kind='bar', figsize=(15,7))

plt.title('CoVid Cases&casualiities Vs  Country Population')

plt.show()


# In[ ]:





# In[47]:


df1.plot(x='continentExp',y=['cases','deaths'], rot=0, figsize=(15,7))

plt.title('CoVid Cases&casualiities Vs  Continent')

plt.show()


# This map shows us that most chances of spreading Covid19 is on American and European countries. 

# In[43]:


df1.plot(x='countryterritoryCode',y=['cases','deaths'], rot=0, figsize=(15,7))

plt.title('CoVid Cases&casualiities Vs  Country ')

plt.show()


# In[46]:


df1.plot(x='countriesAndTerritories',y=['cases','deaths'], rot=0, figsize=(15,7))

plt.title('CoVid Cases&casualiities Vs  Country ')

plt.show()


# This map alarms that the Brazil and some EU contries e.g. Switzerland are more prone to new spread.

# 

# In[52]:


df2 = pd.read_csv('COVID-19 Activity.csv')


# Source of this data is Data world

# In[53]:


df2.head()


# In[19]:


df2.info()


# In[16]:


df2.describe()


# In[54]:


print(round(100*(df2.isnull().sum())/len(df2.index)), 2)


# In[55]:


df2.shape


# In[57]:


df2.isnull().sum()


# In[58]:


(38006/419459)*100


# As we see from above that if we remove all nulls/missing values which will account for about 9-10% of total data. but still we will have about 90% of data which will be sufficient for analysis. hence we will exclude all missing values.

# In[59]:


df2.shape


# In[64]:


df2 = df2.dropna()


# In[65]:


df2.shape


# In[66]:


df2.isnull().sum()


# Now data has no missing values

# In[67]:


df2.head()


# In[71]:



d1 = {'US_PROVINCE_STATE' : df2['PROVINCE_STATE_NAME'],
     'No. of CoVid cases' : df2['PEOPLE_POSITIVE_CASES_COUNT'],
     'No. of New cases' : df2['PEOPLE_POSITIVE_NEW_CASES_COUNT']}

df_plot1 = pd.DataFrame(d1)

df_plot1.plot(x='US_PROVINCE_STATE',y=['No. of CoVid cases','No. of New cases'], figsize=(15,7))

plt.title('CoVid Cases - STATE Vs total cases & new cases')

plt.show()


# This data shows that the US state of florida requires extra resources and precautions in order to control the pandemic.

# In[72]:



d2 = {'US_PROVINCE_STATE' : df2['PROVINCE_STATE_NAME'],
     'No. of CoVid cases' : df2['PEOPLE_POSITIVE_CASES_COUNT'],
     'No. of casualities' : df2['PEOPLE_DEATH_COUNT']}

df_plot2 = pd.DataFrame(d2)

df_plot2.plot(x='US_PROVINCE_STATE',y=['No. of CoVid cases','No. of casualities'], figsize=(15,7))

plt.title('CoVid Cases - STATE Vs total cases & No. of casualities')

plt.show()


# This map shows us that although the spread of pandemic is more on certain states but the no. of casualities are almost similar on all states.

# 

# In[73]:


df3 = pd.read_csv('COVID-19 Cases.csv', low_memory=False)


# Source of this data is Data world.

# In[74]:


df3.head()


# In[20]:


df3.info()


# In[17]:


df3.describe()


# In[79]:


max(round(100*(df3.isnull().sum()/len(df3.index)), 2))


# In[82]:


df3.shape


# In[81]:


df3.isnull().sum()


# In[83]:


len(df3[df3.isnull().sum(axis=1) >1].index)


# In[78]:


import matplotlib.pyplot as plt
NanCol = df3.isnull().sum()
plt.figure(figsize=(20,8))
NanCol.plot(kind='bar')
plt.title('Attributes with Na/missing values')
plt.show() 


# As we see, few attributes with almost all missing values hence they willl account for none analysis and we are excluding.

# In[85]:


df3.head(2)


# In[87]:


df4 = df3[['Case_Type','Cases','Difference','Combined_Key','Country_Region','Province_State','Admin2','Population_Count','Data_Source']]


# In[88]:


df4.head(2)


# In[90]:


df4.shape


# In[89]:


df4.isnull().sum()


# In[91]:


(68886/908418)*100


# As we see max missing values are about 7-8% of total data which if we exclude then we will have about 92% of data left with us, this data will be sufficient for analysis.

# In[92]:


df4.shape


# In[96]:


df4 = df4.dropna()


# In[97]:


df4.shape


# In[98]:


df4.isnull().sum()


# Now we have no missing values.

# In[99]:


df4.head()


# In[106]:


df4.plot(x='Case_Type',y=['Cases','Difference'], rot=0, figsize=(15,7))

plt.title('CoVid Cases Type  Vs  Cases')

plt.show()


# In[101]:


df4.plot(x='Province_State',y=['Cases','Difference'], rot=0, figsize=(15,7))

plt.title('CoVid : Province_State  Vs  Cases')

plt.show()


# This data shows us that at present the spread of pandemic is almost similar across all states.

# In[105]:


df4.plot('Province_State','Cases', figsize=(15,7))

plt.title('CoVid : Province_State  Vs  Cases')

plt.show()


# State wise number of cases.

# In[108]:


df4.plot(x='Province_State',y=['Population_Count','Cases'], rot=0, figsize=(22,9))

plt.title('CoVid : Province_State  Vs  Population_Count & Cases')

plt.show()


# This map shows us that the Population of different states of US and the number of pandemic cases reported. 

# # Conclusion :
# Different visializations helped us to analyze that how the pandemic is sprreading across the world and which areas require extra help and precaustions in order to control the pandemic. although there are much more bigger scope of analysis in this area with more data from different data sources but with the gives time and resources our analysis gives the most valuable highlights on the different spot areas and possibilities of spread of the pandemic.
