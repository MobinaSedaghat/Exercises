#!/usr/bin/env python
# coding: utf-8

# In[39]:


import numpy as np
# import time as time


# In[40]:


def Rdecomp (MD, OD):
    alpha=np.ones(len(MD))
    beta=np.ones(len(OD))
    alpha[0]=(MD[0])**0.5
#     tic=time.time()
    for i in range(len(OD)):
        beta[i]= OD[i]/alpha[i]
        alpha[i+1] = (MD[i+1]-beta[i]**2)**0.5
#     toc=time.time()
    print('alpha= ', alpha, '\n', 'beta= ', beta)
#     print('time= ', toc-tic)


# In[ ]:


while True:
    MD=np.array([int(j) for j in input("Enter your positive symetirc definite main diagonal, for instance: 1,2,3,4,...: \n").split(',')])
    OD=np.array([int(j) for j in input("Enter your positive symetirc definite outer diagonal: \n").split(',')])
#     MD=np.ones(32000000)*32
#     OD=np.ones(31999999)*8
    if len(MD) == len(OD)+1:
        break
    else:
        print("Your given arrays are not valid. Check your input arrays again.")

try:        
    Rdecomp(MD, OD)
except:
    print("Given matrix is not posibble to be decomposed to R and R transposed")

