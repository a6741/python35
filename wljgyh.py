# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 12:31:01 2018

@author: hp
"""
def add(hou,ww):
    max=0
    ii=''
    for k in hou[ww][0]:
        if(hou[k][1]>max):
            max=hou[k][1]
            ii=k
    if(hou[ii][0]!=('')):
        h2[ii]=list(hou[ii])
        h2[ii][1]+=add(hou,ii)
        print(hou[ii][1])
    return max



qian={}
hou={'a':(('g','m'),3),'b':(('h'),4),'c':((''),7),'d':(('l'),3),'e':(('c'),5),'f':(('a','e'),5),'g':(('b','c'),2),'h':((''),5),'i':(('a','l'),2),'k':(('f','i'),1),'l':(('b','c'),7),'m':(('c'),3)}
h2={}
for h in hou:
    if(hou[h][0]!=('')):
        h2[h]=list(hou[h])
        h2[h][1]+=add(hou,h)
for h in hou:
    if(hou[h][0]!=['']):
        for k in hou[h][0]:
            if k in qian.keys():
                qian[k][0].append(h)
                if(qian[k][1]>hou[h][1]):
                    qian[k][1]=hou[h][1]
            else:
                qian[k]=[[h],hou[h][1]]