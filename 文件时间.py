# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 12:19:31 2018

@author: hp
"""
import datetime
import os,time
filepath="C:/Users/hp/Desktop/电子商务大作业"
pathDir =  os.listdir(filepath)
maxtime=0
maxname=''
dic={}
for p in pathDir:
    if(p.split('.')[-1]=='html'):
        #time=time.ctime(os.stat(p).st_mtime)
        a=(time.ctime(os.stat(filepath+'/'+p).st_mtime)).split(' ')[-2]
        d=(time.ctime(os.stat(filepath+'/'+p).st_mtime)).split(' ')[-3]
        times=a.split(':')
        timet=int(times[0])*60*60+int(times[1])*60+int(times[2])+int(d)*24*60*60
        dic[p]=timet
        if(timet>maxtime):
            maxtime=timet
            maxname=p
time1= datetime.datetime.strftime(datetime.datetime.now(),'%Y %m %d %H %M %S')
ntime=time1.split(' ')
nowtime=int(ntime[2])*24*60*60+int(ntime[3])*60*60+int(ntime[4])*60+int(ntime[4])
if(nowtime-maxtime>20*60):
    print('fuck')
else:
    print('yes')