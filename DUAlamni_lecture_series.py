#!/usr/bin/env python
# coding: utf-8

# # Welcome to the DU alumni coding lecture series

# ### Presenters: Bulbul Ahmmed, postdoc at Los Alamos National Laboratory & Dhiman R. Mondal, postdoc at MIT Haystack Observatory

# Mostly stolen from [here](https://nbviewer.jupyter.org/github/rabernat/python_teaching/blob/master/one_day_workshop/01_core_python.ipynb) and [here](https://docs.python.org/3/tutorial/)

# # Lets start with an interesting math problem: Fibonacci Sequence
# ### The Fibonacci sequence is the 1,1,2,3,5,8..., the sum of each number with the preceding one. Lets, write a function about it.

# In[17]:


def fib(n):
    l = [1,1]
    for i in range(n-2):
        l.append(l[-1] + l[-2])
    return l
fib(9)


# ### Variables: need for any kind of coding - Number, string, and boolean
# - Number: Integer, floating, imaginary, etc.
# - String: any kind of texts
# - logical: true and false

# In[8]:


a = 10;
b = "Hello world!"
c = False
print(a)
print(b)
print(type(a))
print(type(b))
print(type(c))


# ## Math

# In[ ]:


# Addition


# In[ ]:


#Subtraction


# In[ ]:


# Multiplication


# In[ ]:


# Division


# In[ ]:


# Exponential


# ## Logical operation
# ## and / or operations

# In[2]:


True and True


# In[3]:


True and False


# In[4]:


False and False


# In[5]:


True or False


# In[6]:


False or True


# ## Conditional statments (if, else, elseif)

# In[12]:


elements = ["K", "Ca"]
element  = "K"
if element == "K":
    print("Alkali Feldspar")
else:
    print("Plagioclase Feldspar")


# In[13]:


x = 100
if x > 0:
    print('Positive Number')
elif x < 0:
    print('Negative Number')
else:
    print ('Zero!')


# ## Flow control (while and for loops)

# In[14]:


# make a loop 
count = 0
while count < 10:
    # bad way
    # count = count + 1
    # better way
    count += 1
print(count)


# In[15]:


# use range
for i in range(5):
    print(i)


# ## Difference between Script and Function
# - Function: You can compile once but can call multiple times without compiling everytime

# In[20]:


xs = [1, 2, 3, 4, 5, 6, 7]
for x in xs:
    print(fib(x))


# ## Python data structures

# In[ ]:


# List: ordered and changeable
x = [1, 2, 3, 4, 5]


# In[32]:


import numpy as np
# Array: Fundamental for scientific computation
A = np.array([1, 2, 3])
A
B = np.random.random((3,2))
B


# In[41]:


# Dictionary: key and value pairs, ordered and changeable
ourdict =	{
  "Geology": "Deals with the subsurface",
  "Physics": "Studies matter",
  "Chemistry": "Studies chemical reaction",
  "Liberation war": 1971
}
ourdict["Geology"]
for (key, val) in ourdict.items():
    print(key, "-->", val)


# In[44]:


# Tuple: ordered and unchangeable, can store multiple data types, and can hadle repetition
tuple1 = ("abc", 34, True, 40, "male")
tuple1


# ## How to use module

# In[39]:


import pandas as pd
#dir(pd)


# In[ ]:




