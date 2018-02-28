# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 15:28:26 2017

@author: hp
"""
import math
mubiao={}
xnumber=int(input('how much x:'))
print("输入目标函数\n")
for i in range(xnumber):
    mubiao['X'+str(i+1)]=input('the x'+str(i+1)+':')
mubiao[0]=input('max or min:')
print("输入约束条件\n")
yues=int(input('how much yueshu:'))
yueshu={}
xiaoy=0
for k in range(yues):
    print('第'+str(k+1)+'个约束式子')
    yueshu[k+1]={}
    for i in range(xnumber):
        yueshu[k+1]['X'+str(i+1)]=input('the x'+str(i+1)+':')
    yueshu[k+1]['fuhao']=input('输入大小符号:')
    if yueshu[k+1]['fuhao']=='<':
        xiaoy+=1
    yueshu[k+1]['b']=input('b值:')
print('目标函数为:')
print(mubiao[0]+'z='+str([str(mubiao[x])+str(x)+'+' for x in mubiao if x]).replace('[','').replace(',','').replace(']','').replace("'",'').replace(' ','').rstrip('+'))
print('约束函数为:')
for num in range(yues):
    print(str([str(yueshu[num+1][x])+str(x)+'+' for x in yueshu[num+1] if x!='fuhao' and x!='b' ]).replace('[','').replace(',','').replace(']','').replace("'",'').replace(' ','').rstrip('+')+yueshu[num+1]['fuhao']+yueshu[num+1]['b'])
omiga={}
M=200000
for i in range(xnumber+yues+xiaoy):
    