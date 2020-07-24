#!/usr/bin/env python
# coding: utf-8

# In[84]:


import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


#Read Cardio Fit data from csv
cdata = pd.read_csv("CardioGoodFitness.csv")


# In[69]:


#Total data 180 
cdata


# In[23]:


(cdata["Gender"] == "Male")


# In[36]:


cdata.info()


# In[243]:


#Plotting pairwise relationships with respect to hue variable
sns.pairplot(cdata, hue = 'Product', palette = "prism_r")


# In[37]:


#Descriptive stats
cdata.describe()


# In[168]:


# We can see below there is positive correlation between customer's predicted usage and miles 
# As well as self rated fitness level and Miles, Education and income
cc = cdata.corr()
sns.heatmap(cc, annot = True)


# In[133]:


# Higher the Education years more is the income and preference for TM798 also increases. 
sns.barplot(x='Education',y='Income',hue="Product",data=cdata) 


# In[149]:


sns.countplot(x="MaritalStatus", hue = "Product", data=cdata)


# In[160]:


#Fewer female customers opt for TM798 model
sns.countplot(x="Product", hue = "Gender", data=cdata, color="red")


# In[163]:


# Higher Fitness rating customers prefer TM798 Model
sns.countplot(x="Fitness",hue = "Product", data=cdata, color = "blue")


# In[170]:


# Higher the fitness level greater the miles targetted ie usage also is higher.
# As seen from above higher fitness customer prefer TM798 Model
sns.swarmplot(x='Fitness', y='Miles', data=cdata, hue = "Product")


# In[247]:


sns.lmplot(x='Income', y = 'Miles', data = cdata, scatter_kws ={'s':20}) #kws to change size


# In[180]:


sns.lmplot(x='Fitness', y = 'Income', data = cdata, hue = "Product", scatter_kws ={'s':20}, palette = "twilight_r") #kws to change size


# In[184]:





# In[189]:


sns.stripplot(x='Fitness', y="Age", data = cdata, hue = "Product")


# In[242]:


sns.lmplot(x='Age', y = 'Fitness', data = cdata, col= "Product", aspect = 0.6, height = 5, hue = "Gender", palette="magma")


# In[ ]:




