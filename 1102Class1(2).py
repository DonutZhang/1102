
# coding: utf-8

# In[2]:

#串列
mar = ['a','b','c']
mar[2] = 'relace'
mar


# In[3]:

mar[0:2]


# In[5]:

mar.append('new')
mar


# In[7]:

others = ['1','2','3']
mar += others
mar


# In[8]:

# append:將項目加到結尾
mar2 = ['aa','bb','cc']
mar2.append(others)
mar2


# In[13]:

#insert:插入項目
mar3 = ['aa','bb','cc']
mar3.insert(2,'try')
mar3


# In[16]:

# extend:結合串列
mar4 = ['a','c']
mar4.extend(others)
mar4


# In[18]:

#del:remove項目
del mar4[-1]
mar4


# In[24]:

mar5 = ['11','22','33','44']
mar5 [2]


# In[28]:

#del []
del mar5 [2]
mar5


# In[27]:

mar5[2]


# In[31]:

#remove : 不確定位置，直接輸入欲刪除值
mar6 = ['qq','w','r']
mar6.remove('w')
mar6


# In[33]:

#pop():從串列取值並刪除他
mar7 = ['1','2','3','a','b','c']
mar7.pop()


# In[34]:

mar7.pop(1)


# In[35]:

mar7


# In[36]:

#in : 檢查船列中是否有"值"
mar8 = ['a','b','c']
'b' in mar8


# In[37]:

'e' in mar8


# In[40]:

#index:用"值"搜尋其在串列中的位置
mar8.index('b')


# In[ ]:



