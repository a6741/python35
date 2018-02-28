# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 23:05:58 2017

@author: hp
"""

# coding:utf-8
import datetime
import itchat
import math
import re
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import os
import numpy as np
import PIL.Image as Image
from PIL import ImageDraw,ImageFont
global dst  
dst=os.path.join(os.path.expanduser("~"), "Desktop")
plt.rcParams['font.sans-serif']=['SimHei'] 
plt.rcParams['axes.unicode_minus']=False
global fontpat
fontpat='simhei.ttf'#据说win10的字体后缀是ttc，请自行更改
def getinformation(fwants,mwants,cloudpic):
    picpath=dst+'/information'
    if not os.path.exists(picpath):
        os.mkdir(picpath)#创造文件存放路径
    global friends,mpsList,fontpat
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
    y=1.5
    wname="Official Accounts'"
    image=Image.new('RGBA',(ws,hs),(255,255,255))
    imaloc={}
    for ttur in range(2):
        for want in wants.keys():
            if wants[want]==0:
                text[want] = "".join(tList[want+tags])
                im=makecloud(cloudpic,text[want],wname+' '+want)
                imaloc['the cloud of\n'+wname+' '+want]=(x*hb,y*hb)
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
            image.paste(im,(x*hb,int(y*hb)))
            x+=1
            if x==2:
                x=0
                y+=1
        wants=fwants
        List=friends
        tags='f'
        wname="friends's"
        if x!=0:
            y+=1
            x=0
    allhead=picconnect(picpath)
    leng=min(hs-hb*y,ws)
    allhead=allhead.resize((leng,int(leng*(allhead.height/allhead.width)+0.5)), Image.ANTIALIAS)
    if x!=0:
        y+=1
        x=0
    image.paste(allhead,(x*hb,int(y*hb)))
    draw = ImageDraw.Draw(image)
    font2 = ImageFont.truetype(fontpat,28)
    font1 = ImageFont.truetype(fontpat,96)
    draw.text((hb//3*2,0), '   a\n simple\nanalysis\n   of\n  your\n wechat', (255, 0, 0),font=font1)    #设置文字位置/内容/颜色/字体
    for i in imaloc:
        draw.text(imaloc[i],i, (255, 0, 0),font=font2)
    draw = ImageDraw.Draw(image)
    image.save(picpath + "/" + "analysis.png")
def makecloud(pic,text,want):
    
    wordlist_jieba = jieba.cut(text, cut_all=False)
    wl_space_split = " ".join(wordlist_jieba)
    print("没有死机，程序还在执行")
    # wordcloud词云
    d= os.path.dirname(os.path.abspath( __file__ ))
    alice_coloring = np.array(Image.open(os.path.join(d,pic)))
    #global fontpat
    #
    my_wordcloud = WordCloud(background_color="white", max_words=100,mask=alice_coloring,max_font_size=400, random_state=420,font_path=fontpat).generate(wl_space_split)
    image_colors = ImageColorGenerator(alice_coloring)
    plt.imshow(my_wordcloud.recolor(color_func=image_colors))
    plt.imshow(my_wordcloud)
    plt.axis("off")
    im = im = Image.fromarray(np.array(my_wordcloud))
    im.putpixel((200,200),200)
    draw = ImageDraw.Draw(im)
    print(draw)
    return im
def getallhead(path):
    for i in friends:
        img = itchat.get_head_img(userName=i["UserName"])
        try:
            with open(path+"/"+i["NickName"]+".png","wb") as f:
                f.write(img)
        except:
            print('wrong in ',i["NickName"])
def picconnect(picpath):
    howb=1280
    getallhead(picpath)
    ls = os.listdir(picpath)
    each_size = int(math.sqrt(float(howb*howb)/len(ls)))
    lines = int(howb/each_size)
    howb=each_size*lines
    image = Image.new('RGBA', (howb, howb+2*each_size),(255,255,255))
    x = 0
    y = 0
    for pic in ls:
        try:
            global img
            img = Image.open(picpath+'/'+pic)
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
    starttime = datetime.datetime.now()
    itchat.login()
    print("这个程序可能执行得很慢(在我电脑上有时要等上七八分钟)，我暂时也不知道为什么，因为我一开始写的时候忘记加注释了，所以可能看着很臃肿")
    global friends,mpsList
    friends = itchat.get_friends(update=True)[0:]
    mpsList=itchat.get_mps(update=True)[0:]
    getinformation({'City':0,'Sex':1,'Signature':0},{'NickName':0,'Signature':0},r"123.png")
    endtime = datetime.datetime.now()
    print (endtime - starttime)