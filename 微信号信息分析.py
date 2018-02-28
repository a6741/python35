# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 23:05:58 2017

@author: hp
"""

# coding:utf-8
import itchat
import math
import re
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import os
import numpy as np
import PIL.Image as Image
from PIL import ImageDraw
dst=os.path.join(os.path.expanduser("~"), "Desktop")
global dst
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False
def getinformation(fwants,mwants,cloudpic):
    picpath=dst+'\\'+'information'
    if not os.path.exists(picpath):
        os.mkdir(picpath)
    global friends,mpsList
    tList={}
    text={}
    tab={}
    wants=fwants
    List=friends
    tags='f'
    for tur in range(2):
        for want in wants.keys():
            tList[want+tags]=[]
            text[want+tags]=[]
            tab[want+tags]={}
        for i in List:
            for want in wants.keys():
                if wants[want]==0:
                    signature=i[want].replace(" ", "").replace("span", "").replace("class", "").replace("emoji", "")
                    rep=re.compile("1f\d.+")
                    signature= rep.sub("", signature)
                    tList[want+tags].append(signature)
                elif wants[want]==1:
                    if i[want] not in tab[want+tags]:
                        tab[want+tags][i[want]]=0
                    tab[want+tags][i[want]]+=1
        wants=mwants
        List=mpsList
        tags='m'
    ws=1024
    hs=4096
    hb=ws//2
    x=0
    y=0
    image=Image.new('RGBA',(ws,hs),(255,255,255))
    for ttur in range(2):
        for want in wants.keys():
            if wants[want]==0:
                text[want] = "".join(tList[want+tags])
                im=makecloud(cloudpic,text[want],want)
            elif wants[want]==1:
                im=maketab(tab[want+tags])
            mi=min(im.size)
            miloc=(im.size).index(mi)
            ma=max(im.size)
            basi=[0,0]
            basi[miloc]=ma-mi
            basi[1-miloc]=ma
            im=im.crop((0,0,max(im.size),max(im.size)))
            baim=Image.new('RGBA',tuple(basi),(255,255,255))
            pasi=[0,0]
            pasi[miloc]=mi
            im.paste(baim,tuple(pasi))
            im=im.resize((hb,hb), Image.ANTIALIAS)
            image.paste(im,(x*hb,y*hb))
            x+=1
            if x==2:
                x=0
                y+=1
        wants=fwants
        List=friends
        tags='f'
    allhead=picconnect(picpath)
    leng=min(hs-hb*y,ws)
    allhead=allhead.resize((leng,leng), Image.ANTIALIAS)
    if x!=0:
        y+=1
        x=0
    image.paste(allhead,(x*hb,y*hb))
    image.save(picpath + "/" + "analysis.png")
def makecloud(pic,text,want):
    wordlist_jieba = jieba.cut(text, cut_all=False)
    wl_space_split = " ".join(wordlist_jieba)
    # wordcloud词云
    d= os.path.dirname(os.path.abspath( __file__ ))
    alice_coloring = np.array(Image.open(os.path.join(d,pic)))
    my_wordcloud = WordCloud(background_color="white", max_words=2000,mask=alice_coloring,max_font_size=400, random_state=420,font_path=r'C:\Windows\Fonts\simhei.ttf').generate(wl_space_split)
    image_colors = ImageColorGenerator(alice_coloring)
    plt.imshow(my_wordcloud.recolor(color_func=image_colors))
    plt.imshow(my_wordcloud)
    plt.axis("off")
    im = im = Image.fromarray(np.array(my_wordcloud))
    return im
def getallhead(path):
    for i in friends:
        img = itchat.get_head_img(userName=i["UserName"])
        with open(path+"\\"+i["NickName"]+".png","wb") as f:
            f.write(img)
def picconnect(picpath):
    getallhead(picpath)
    howb=1280
    ls = os.listdir(picpath)
    each_size = int(math.sqrt(float(howb*howb)/len(ls)))
    lines = int(howb/each_size)
    image = Image.new('RGBA', (howb, howb))
    x = 0
    y = 0
    for pic in ls:
        try:
            img = Image.open(picpath+'\\'+pic)
            global img
        except IOError:
            print("Error in "+pic)
        else:
            img = img.resize((each_size, each_size), Image.ANTIALIAS)
            image.paste(img, (x * each_size, y * each_size))
            x += 1
            if x == lines:
                x = 0
                y += 1
    return image
def maketab(lis):
    labels='性别不明','男','女'
    bili=list(lis.values())
    plt.axes(aspect=1)#使x y轴比例相同    
    explode=[0,0,0]# 突出某一部分区域 
    plt.rc('font',size=20)
    plt.pie(x=bili,labels=labels,autopct='%.0f%%',explode=explode)
    f=plt.gcf()
    f.canvas.draw()
    data = np.fromstring(f.canvas.tostring_rgb(), dtype=np.uint8, sep='')
    data = data.reshape(f.canvas.get_width_height()[::-1] + (3,))
    return Image.fromarray(data)    
if __name__ == "__main__":
    itchat.login()
    friends = itchat.get_friends(update=True)[0:]
    mpsList=itchat.get_mps(update=True)[0:]
    global friends,mpsList
    getinformation({'City':0,'Sex':1,'Signature':0},{'City':0,'NickName':0,'Signature':0},"123.png")