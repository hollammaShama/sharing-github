#!/usr/bin/env python
# coding: utf-8

# In[2]:


import json
import re
from collections import Counter


listt=[]
listy=[]
#<----------------reading both files--------------------->
with open('t.json', 'r+') as fp:
        for line in fp:
            listt.append(json.loads(line))


with open('y.json', 'r+') as tp:
        for line in tp:
            listy.append(json.loads(line))
fp.close()
tp.close()
#<------------combine values of the two files--------->
listtotal=listt+listy

#<-------------------------for adding values to category and subcategories in listtotal---->

listcate1=[]
listcate2=[]
listsubcate1=[]
listsubcate2=[]

for x in listt:
    listcate1.append(x['category'])
    listsubcate1.append(x['subcategory'])

for y in listy:
    listcate2.append(y['category'])
    listsubcate2.append(y['subcategory'])


#<----------- in order to filter out duplicates and combine categories and subsets of both files--->
categoryuniqueset= list(set(listcate1)|(set(listcate2)))   
#print(categoryuniqueset)
subcategoryuniqueset=set(listsubcate1).intersection((listsubcate2))
totalsubcate=listsubcate1+listsubcate2
subcatfrequency=Counter(totalsubcate)      #frequency of each subcategory

for line in listtotal:
    if line['category'] in categoryuniqueset and line['subcategory'] in subcategoryuniqueset:
        print(line['category'] + " > " + line['subcategory'] + ": " + str(subcatfrequency[line['subcategory']]))
        subcategoryuniqueset.remove(line['subcategory'])   #remove subcat once printed 


# In[ ]:




