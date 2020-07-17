#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd  
  

data_dict = {'Chips':['Simba', 'Lays'], 
            'Cooldrinks':['Coke', 'Fanta'], 
            'Chocolates':['Cadbury', 'Tex'],
            'Pies':['Pepper Steak', 'Chicken'],
            'Fruit':['Pear', 'Apple'],
            'Cupcakes':['Vanilla', 'Chocolate'],
            'Veggies':['Spinach', 'Cabbage']
             }

dFrame = pd.DataFrame(data_dict)
dFrame
  


# In[ ]:


dFrame.index


# In[ ]:


dFrame.columns # adding columns


# In[2]:


Meats = ['Pork', 'Beef']  # the addition of more products
dFrame['Meats'] = Meats

dFrame


# In[ ]:


grouped = dFrame.groupby(dFrame.Chips)

Simba = grouped.get_group("Simba")



# Still experiencing issues with MySQL


# In[ ]:




