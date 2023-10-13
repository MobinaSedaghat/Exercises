#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
# import time as time


# In[3]:


def TridMult(a, c, e, v):
    answer=np.zeros(len(a))
    c=np.append(c,0)
    v=np.append(v,0)
    e=np.append(e,0)
    e=np.insert(e,0,0,0)
#     tic=time.time()
    for i in range(len(a)):
        answer[i]=(a[i]*v[i]+c[i]*v[i+1]+e[i]*v[i-1])
#     toc=time.time()
    print('answer= ', answer)
#     print('time= ', toc-tic)


# In[ ]:


while True:
    a=np.array([int(j) for j in input("Enter your a array, for instance: 1,2,3,4,...: \n").split(',')])
    e=np.array([int(j) for j in input("Enter your e array: \n").split(',')])
    c=np.array([int(j) for j in input("Enter your c array: \n").split(',')])
    v=np.array([int(j) for j in input("Enter your v array: \n").split(',')])
#     a=np.ones(40000000)
#     c=np.ones(39999999)
#     v=np.ones(40000000)
#     e=np.ones(39999999)
    if len(a) == len(v) and len(a) == len(e)+1 and len(a) == len(c)+1:
        break
    else:
        print("Your given arrays are not valid. Check your input arrays again.")

TridMult(a,c,e,v)

