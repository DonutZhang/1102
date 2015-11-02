
# coding: utf-8

# In[2]:

#join : 用ｊｏｉｎ以符號做結合
mar = ['try','hard','ed']
'*'.join(mar)


# In[4]:

#sorted() : 排序並回傳副本
sorted_mar = sorted(mar)
sorted_mar


# In[6]:

#sort:排序
mar.sort()
mar


# In[8]:

mar2 = ['1','3','2']
mar2.sort()
mar2


# In[9]:

#reverse = True :降幕
num = ['2','1','3','4']
num.sort(reverse=True)
num


# In[11]:

num.sort()
num


# In[12]:

# = :指派
a = [1,2,3]
a


# In[14]:

b = a 
b


# In[16]:

a[0] = 'sup'
a


# In[17]:

b


# In[19]:

b[0] = 'I eat'
b


# In[20]:

a


# In[24]:

#copy() : 複製 ; list() :轉換
a = [1,2,3]
b = a.copy()
c = list(a)
d = a[:]

a[0] = 'boring'

a


# In[25]:

b


# In[26]:

c


# In[27]:

d


# In[28]:

#tuple
empty_tuple = ()
empty_tuple


# In[30]:

one_marx = 'Gro',
one_marx


# In[31]:

marx_tuple =('D','S','A')
marx_tuple


# In[33]:

a, b, c = marx_tuple
a


# In[34]:

b


# In[35]:

c


# In[36]:

# tuple交換
password = 'sw'
icecream = 'cho'
password, icecream = icecream, password
password


# In[37]:

icecream


# In[38]:

marx_list = ['qaq','cho','ha']
tuple(marx_list)


# In[ ]:



