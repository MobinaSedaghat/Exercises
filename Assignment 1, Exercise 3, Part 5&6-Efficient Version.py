#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
# import time as time


# In[7]:


def Linsolver(alpha, beta, c, B):
    y=np.ones(len(B))
    y[0]=B[0]
#     tic=time.time()
    for i in range(len(B)-1):
        y[i+1]=B[i+1]-beta[i]*y[i]
    print('y=', y)
    y=y[::-1]
    c=c[::-1]
    alpha=alpha[::-1]
    x=np.ones(len(B))
    x[0]=y[0]/alpha[0]
    for i in range(len(y)-1):
        x[i+1]=(y[i+1]-c[i]*x[i])/alpha[i+1]
    x=x[::-1]
#     toc=time.time()
    print('x=', x)
#     print('time= ', toc-tic)


# In[ ]:


while True:
    
    alpha=np.array([int(j) for j in input("Enter your alpha array, for instance: 1,2,3,4,...: \n").split(',')])
    beta=np.array([int(j) for j in input("Enter your beta array: \n").split(',')])
    c=np.array([int(j) for j in input("Enter your c array: \n").split(',')])
    B=np.array([int(j) for j in input("Enter your right-hand-side array, B: \n").split(',')])
#     alpha=np.ones(20000000)
#     beta=np.ones(19999999)
#     B=np.ones(20000000)
#     c=np.ones(19999999)
    if len(alpha) == len(beta)+1 and len(alpha) == len(c)+1 and len(B) == len(alpha):
        break
    else:
        print("Your given arrays are not valid. Check your input arrays again.")

Linsolver(alpha, beta, c, B)

