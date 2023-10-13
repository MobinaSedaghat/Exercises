#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
# import time as time


# In[9]:


def LUdecomp(a,c,e):
    beta=np.zeros(len(c))
    alpha=np.zeros(len(a))
    alpha[0]=a[0]
#     tic=time.time()
    for i in range (len(e)):
        beta[i]=e[i]/alpha[i]
        alpha[i+1]=a[i+1]-beta[i]*c[i]
#     toc=time.time()
    print('alpha= ', alpha, '\n', 'beta= ', beta)
#     print('time= ', toc-tic)


# In[ ]:


while True:
    a=np.array([int(j) for j in input("Enter your a array, for instance: 1,2,3,4,...: \n").split(',')])
    e=np.array([int(j) for j in input("Enter your e array: \n").split(',')])
    c=np.array([int(j) for j in input("Enter your c array: \n").split(',')])
#     a=np.ones(800000)*5
#     c=np.ones(799999)*3
#     e=np.ones(799999)*4
    if len(a) == len(e)+1 and len(a) == len(c)+1:
        break
    else:
        print("Your given arrays are not valid. Check your input arrays again.")


LUdecomp(a,c,e)

