# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
import re
import xlrd
import xlwt
data=xlrd.open_workbook(r'C:\Users\hp\Desktop\1.xlsx')
sheet=data.sheets()[0]
dic={}
loc={}
ndi={}
tdic={}
time=[8,9,10,11,14,15,16,17,19,20]
for i in range(1,sheet.nrows):
    k=sheet.cell(i,3).value
    if k=='':
        pass
    else:
        nu=1
        while k+str(nu) in dic:
            if loc[dic[k+str(nu)]]!=sheet.cell(i,2).value:
                nu+=3
            else:
                nu+=1
        k+=str(nu)
        dic[k]=re.search('套班\w+',sheet.cell(i,1).value).group()
        loc[re.search('套班\w+',sheet.cell(i,1).value).group()]=sheet.cell(i,2).value
for i in dic:
    name=re.search('\w+[^0-9]',i).group()
    tim=int(re.search('\w$',i).group())
    if name not in ndi:
      ndi[name]=[]
    if dic[i] not in tdic:
        tdic[dic[i]]={}
    #print('!!!!',time[tim%10])
    #print('???',ndi[name])
    flag=1
    uuu=0
    while time[tim%10] in ndi[name] or time[tim%10] in tdic[dic[i]].keys() or flag==0:
        flag=1
        uuu=0
        tim+=1
        if {time[(tim-1)%10]:name} in tdic.values():
            restr='[^{}]*'+str(time[(tim-1)%10])+": '"+name+"'[^{}]*(?=\})"
            ind='{'+re.findall(restr,str(tdic.values()))[0]+'}'
            recentloc=loc[list(tdic.keys())[list(tdic.values()).index(eval(ind))]]
            if recentloc!=loc[dic[i]]:
                rec=recentloc
            uuu=1
        if {time[(tim+1)%10]:name} in tdic.values():
            restr='[^{}]*'+str(time[(tim+1)%10])+": '"+name+"'[^{}]*(?=\})"
            ind='{'+re.findall(restr,str(tdic.values()))[0]+'}'
            recentloc=loc[list(tdic.keys())[list(tdic.values()).index(eval(ind))]]
            if recentloc!=loc[dic[i]]:
                rec=recentloc
            uuu=1
        if uuu!=1:
            rec=loc[dic[i]]
        if rec!=loc[dic[i]]:
            tim+=2
            flag=0
        print(rec,loc[dic[i]])
        '''for nst in ndi[name]:
            if nst==time[tim%10]-1 or nst==time[tim%10]+1:
            #if {nst:name} in list(tdic.values()):
                 for ss in list(tdic.values()):
                    if nst in ss and ss[nst]==name:
                        ind=ss
                 if loc[dic[i]]!=list(tdic.keys())[list(tdic.values()).index(ind)]:#有问题
                     tim+=1'''
    tdic[dic[i]][time[tim%10]]=name
    ndi[name].append(time[tim%10])
book=xlwt.Workbook()
sh=book.add_sheet('yes')
h=1
sh.write(0,0,'地址')
sh.write(0,1,'班级')
sh.write(0,2,'老师')
sh.write(0,3,'时间')
for li in tdic:
    for k in tdic[li]:
        sh.write(h,1,li)
        sh.write(h,2,tdic[li][k])
        sh.write(h,3,str(list(tdic[li].keys())[list(tdic[li].values()).index(tdic[li][k])])+':00')
        sh.write(h,0,loc[li])
        h+=1
book.save(r'C:\Users\hp\Desktop\summy.xls')
     
