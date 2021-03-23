#!/usr/bin/env python
# coding: utf-8

# In[24]:


def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    return K[n][W], K          


# In[27]:


val = [1,2,5,6]
wt = [2,3,4,5]
W = 8
n = len(val)
score, K = knapSack(W, wt, val, n)
print("score is :",score)
for row in K:
    for e in row:
        print(e, end = '  ')
    print()


# In[ ]:




