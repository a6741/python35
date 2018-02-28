# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 20:01:19 2017

@author: hp
"""
import time
import requests ##导入requests
from bs4 import BeautifulSoup ##导入bs4中的BeautifulSoup
import os
from selenium import webdriver
dst="C:\\Users\\hp\\Desktop\\电子商务html\\产品清单\\"
kk="<div class='goods'><img class='goodsimg' src='{0}' />{1}<br />仅售<b>{2}</b></div><div class='block'>&nbsp;</div>"
tt=1
txt=""
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
for page in range(1,2):
    all_url="http://shop.lelezone.com/category-119-b0-min0-max0-attr0-"+str(page)+"-goods_id-DESC.html"
    shtml=requests.get(all_url,headers=headers)
    Soup=BeautifulSoup(shtml.text,'lxml')
    a=Soup.find('ul',class_="list-h").find_all('li')
    for aa in a:
        k=aa.find(class_="p-img").find('a').find('img')
        name=aa.find(class_='p-name').find('a').get_text()
        price=aa.find(class_="p-price").get_text().replace("￥","")
        srcc=k['src']
        img = requests.get(srcc, headers=headers)
        f = open(dst+str(tt)+'.jpg', 'ab')##写入多媒体文件必须要 b 这个参数！！必须要！！
        f.write(img.content) ##多媒体文件要是用conctent哦！
        f.close()
        kkk=kk.format("产品清单/"+str(tt)+'.jpg',name,price)
        txt+=kkk
        txt+="\n"
        if(tt%4==0):
            txt+="<div class='goods'>&nbsp;</div>"
            txt+="<div class='goods'>&nbsp;</div>"
            txt+="<div class='goods'>&nbsp;</div>"
            txt+="<div class='goods'>&nbsp;</div>"
        tt+=1