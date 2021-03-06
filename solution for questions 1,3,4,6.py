#!/usr/bin/env python
# coding: utf-8

# In[5]:


import json
import pandas as pd
from collections import Counter
#<------ read the file as a dataframe using pandas------->

df1=pd.read_json('t.json', lines=True)
df3=pd.read_json('y.json', lines=True)


#<-------------list of urlh overlapping.--------------------------->
#<-----------access urlh column from both dataframes----->
urlhcol1=df1.loc[:,"urlh"]
urlhcol2=df3.loc[:,"urlh"]

urlhlist1= list(urlhcol1)
print("length of file t.json", len(urlhlist1))
urlhlist2= list(urlhcol2)
print("length of file y.json", len(urlhlist2))
#<-----------overlapping urlh-------- sets so that there is no duplicates--->
overlap = list(set(urlhlist1) & set(urlhlist2))
#print(overlap)
#print(len(overlap))
print("length of overlapping urlh in both files is :", len(set(overlap)))

print("\n<----------------------------------------------------------------------------------->")

#<-------------No of Unique categories in both files.------------------------------>
      #<--------access category column from dataframe----->
df2=df1.loc[:,"category"]
l1=list(df2)
#print (l1)

#dict1={x:l1.count(x) for x in l1}
#print (dict1)
c=Counter(l1)                                                          #using dictionaries 
uniquecat=c.keys()
uniquecat=set(uniquecat)
print("\nlist of unique categories of file t.json \n")
print(uniquecat)
print(" \n\nnumber of unique category in file t.json",len(uniquecat))


print("\n \n \n")



df4=df3.loc[:,"category"]
l2=list(df4)
s=set(l2)                                                              #using sets
print("list of unique categories of file y.json \n")
print(s)
print("\nnumber of unique category in file y.json",len(s))
print("\n<---------------------------------------------------------------------------------->")

#<-------------list of categories not overlapping.-------------->

listunique=[]
listunique= (list(set(l1) - set(l2))) 
print("\n\ncategories NOT overlapping are :",listunique)
print(" \nnumber of categories NOT overlapping \n ",len(listunique))
print("<------------------------------------------------------------------------------------->")


#<-------------Create 2 different new files for normalized mrps .--------------> assuming 2 different files to be created. files only for normalised mrps

mrp1=df1.loc[:,"mrp"]
mrp2=df3.loc[:,"mrp"]

d1=mrp1.to_dict()
#ke=list(d1.keys())
for i in d1.keys():
    if d1[i]==0.0 or d1[i]== "nan" or d1[i].is_integer():
        d1[i]="N/A"
    
#print(d1)
with open('normalisedtjson.json', 'w') as fp:
    json.dump(d1, fp)
print("\nfile normalisedtjson.json is created\n\n")
fp.close()

d2=mrp1.to_dict()
#ke=list(d1.keys())
for j in d2.keys():
    
    if d2[j]==0.0 or d2[j]== "nan" or d2[j].is_integer():
        d2[j]="N/A"

        
#print(d2)
with open('normalisedyjson.json', 'w') as tp:
    json.dump(d2, tp)
print("file normalisedyjson.json is created\n\n")
tp.close()


  







