#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json
import re
from collections import Counter

listt=[]
listy=[]
with open('t.json', 'r+') as fp:
        for line in fp:
            listt.append(json.loads(line))


with open('y.json', 'r+') as tp:
        for line in tp:
            listy.append(json.loads(line))
fp.close()
tp.close()

listtotal=listt+listy

urlht=[]
urlhy=[]
for x in listt:
    urlht.append(x['urlh'])
    

for y in listy:
    urlhy.append(y['urlh'])
    

overlapping= set(set(urlht) & set(urlhy))
o=list(overlapping)                 
print("overlapping urlh count:", len(o))


for x in listt:
    urlht.append(x['available_price'])
    

for y in listy:
    urlhy.append(y['available_price'])

newlist=[]
newerlist=[]

for n in range(len(listt)):
    if listt[n]['http_status']== "200":
        newlist.append(listt[n])
for p in range(len(listy)):
    if listy[p]['http_status']== "200":
        newerlist.append(listt[p])




print("price difference :")
for value in listt:
    for val in listy:
        if  value['urlh'] == val['urlh'] and value['urlh'] in overlapping:
            price1=value['available_price']
            price2=val['available_price']
            if price1 != None and price2 != None:       #because nothing has to be done if prices not given
                
                num1=float(price1)
                num2=float(price2)
                if num1 !=num2:                         #just to ensure absence of multiple zeros, making answer compact
                    res=("%.2f"% abs(num1-num2))
                
                    print(res)
                overlapping.remove(value['urlh'])
            break;


# In[ ]:





# In[ ]:




