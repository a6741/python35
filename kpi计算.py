# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 18:06:56 2017

@author: hp
"""
import os
import pandas as pd
a=[]
b=[]
p=[]
jinji={}
bumen={}
name='nan'
for isa in os.listdir(r'C:/Users/hp/Desktop/trydata/'):
    print(isa)
    k=pd.read_excel(r'C:/Users/hp/Desktop/trydata/'+isa)
    k['紧急活动']=k['紧急活动'].fillna(0)
    k=k.dropna(axis=0,thresh=3).dropna(axis=1,thresh=2)
    #print(k)
    k=k.drop('总分',1)
    k=k[(True-k['部员姓名'].isin(['部门成员平均分']))]
    for i in k:
        if 'Unnamed' in i:
            k=k.rename(columns={i: name+'1'})
        name=i
    for i in range(len(k['部员姓名'])):
         try:
             k.iloc[i,0]=k.iloc[i,0].replace(' ','')
         except:
             pass
    if k.iloc[0,1]=='出勤会议':
        k['部门']=isa.replace('.xlsx','')+'部'
        a.append(k)
    else:
        b.append(k) 
cols=['部门','部员姓名','部门工作','部门工作1','品牌活动打分','品牌活动打分1','紧急活动']
for i in a:
    for k in b:
            t=pd.merge(i.drop('紧急活动',1),k.drop('紧急活动',1),how = 'outer')
            t=t.dropna(axis=0,thresh=5)
            t['紧急活动']=pd.merge(i,t,how = 'outer')['紧急活动']+pd.merge(k,t,how = 'outer')['紧急活动']
            #t.s
            if (len(i.loc[i["紧急活动"] == 1])!=0):
                jinji[str(i.loc[i["紧急活动"] == 1])]=1
            if(len(k.loc[k["紧急活动"] == 1])!=0):
                jinji[str(k.loc[k["紧急活动"] == 1])]=1
            print()
            t['紧急活动']=t['紧急活动'].fillna(0)
            t = t.ix[:, cols]
            p.append(t)
for u in p:
    u=u.dropna(axis=0,thresh=7)
    t=t.append(u)
t=t.drop_duplicates()
t.to_excel(r'C:/Users/hp/Desktop/1.xlsx')
for i in jinji:
    print(i)
