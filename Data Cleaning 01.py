
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm',
'Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
'12. Air France', '"Swiss Air"']})


# In[3]:


df


# In[4]:


# 1. Some values in the the FlightNumber column are missing. These numbers are meantto increase by 10 with each row so 10055 and 10075 need to be put in place. Fill in these missing numbers and make the column an integer column (instead of a float column)

# Replacing NAN values with the preceding values + 10 in FlightNumber Column

for i in range(df.FlightNumber.count() + 1):
    print(df.FlightNumber.loc[i,])
    if pd.isnull(df.FlightNumber.loc[i,]):
        df.loc[i,'FlightNumber'] = df.FlightNumber.loc[i-1,] + 10
        print(df.FlightNumber.loc[i,])


# In[5]:


df


# In[6]:


# 2. The From_To column would be better as two separate columns! Split each string onthe underscore delimiter _ to give a new temporary DataFrame with the correct values.Assign the correct column names to this temporary DataFrame.

df_tmp = df.copy()
df_tmp[['From','To']] = df_tmp.From_To.str.split("_",expand=True)


# In[7]:


df


# In[8]:


df_tmp


# In[9]:


# 3. 3. Notice how the capitalisation of the city names is all mixed up in this temporaryDataFrame. Standardise the strings so that only the first letter is uppercase (e.g."londON" should become "London".)

print(df_tmp)
df_tmp.From = df_tmp.From.str.capitalize()
df_tmp.To = df_tmp.To.str.capitalize()
df_tmp.From_To = df_tmp.From_To.str.capitalize()
print('-'*80)
print(df_tmp)


# In[10]:


# 4.Delete the From_To column from df and attach the temporary DataFrame from theprevious questions.

print(df)
df.drop('From_To',axis=1,inplace=True)
print('-'*80)
print(df)
df['From_To'] = df_tmp['From_To']
print('-'*80)
print(df)


# In[11]:


# 5. In the RecentDelays column, the values have been entered into the DataFrame as alist. We would like each first value in its own column, each second value in its owncolumn, and so on. If there isn't an Nth value, the value should be NaN.

rows = []
_ = df.apply(lambda row: [rows.append([row['Airline'], row['FlightNumber'],nn,row['From_To']]) 
                         for nn in row.RecentDelays], axis=1)


# In[12]:


rows


# In[13]:


df_new = pd.DataFrame(rows, columns=df.columns)


# In[14]:


print("Original DataFrame :  \n")
print(df)
print('*'*80)
print("New DataFrame :  \n")
print(df_new)


# In[15]:


# Expand the Series of lists into a DataFrame named delays, rename the columns delay_1,delay_2, etc. and replace the unwanted RecentDelays column in df with delays.


df3 = pd.DataFrame(df['RecentDelays'].values.tolist())


# In[16]:


df3


# In[17]:


length_cols = df3.shape[1]


# In[18]:


length_cols


# In[19]:


df3.columns[0]


# In[20]:


col_list = []
col_dict ={}
for i in range(length_cols):
    Key = df3.columns[i]
    #print(key,i)
    Value = "Delay" + str(i+1)
    col_dict[Key] = Value


# In[21]:


col_dict


# In[22]:


df3.rename(columns=col_dict,inplace=True)


# In[23]:


df3


# In[24]:


df[["Delay1","Delay2","Delay3"]] = df3[["Delay1","Delay2","Delay3"]]


# In[25]:


print(df)
print('*'*80)
df.drop('RecentDelays', axis=1, inplace=True)
print(df)


# In[26]:


# Finally changed DataFrame looks like:

df

