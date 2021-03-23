#!/usr/bin/env python
# coding: utf-8

# In[1]:


n = int(input("Enter the number of items -> "))
sack = int(input("Enter the sack size -> "))


# In[2]:


class knapsack_object():
    def __init__(self, num):
        self.number = num
        self.profit = int(input("Enter the profit -> "))
        self.weight = int(input("Enter the weight -> "))
        self.ratio = self.profit / self.weight
        self.kept = 0


# In[3]:


def display(obj):
    for o in obj:
        print('object no. - ',o.number,' profit -',o.profit,' weight -',o.weight,' ratio -',o.ratio,' kept -',o.kept)


# In[4]:


obj = []
for i in range(n):
    print('--->for',i + 1,'instance')
    obj.append(knapsack_object(i + 1))
    print('-'*30)


# In[5]:


display(obj)


# In[6]:


def knapsack_greedy_approach(obj, sack):
    obj = sorted(obj,key=lambda x:(x.ratio),reverse=True)
    for o in obj:
        if sack == 0:
            break
        if sack >= o.weight:
            o.kept = 1
            sack -= o.weight
    if sack !=0:
        for o in obj:
            if o.kept == 0:
                o.kept = sack/o.weight
                sack -= (sack/o.weight) * o.weight


# In[7]:


knapsack_greedy_approach(obj, sack)


# In[8]:


display(obj)


# In[ ]:




