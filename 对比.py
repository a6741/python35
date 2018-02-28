# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 22:16:27 2017

@author: hp
"""
web="http://twi.xmu.edu.cn/vms/xmuzyz/index.php/ytw/bmqk/"+input("请输入活动编号\n")
exceladd=input(r"文件路径，如 C:\Users\hp\Desktop\管院青协 研究生迎新工时表.xlsx 这样"+"\n这个面板不能复制我也不知道为什么，建议可以把excel表复制到这个目录下面，然后直接输入比如 管院青协 研究生迎新工时表.xlsx 也同样可以\n")
#C:\Users\hp\Desktop\管院青协 研究生迎新工时表.xlsx
import pandas 
from selenium import webdriver
driver = webdriver.PhantomJS(executable_path="phantomjs-2.1.1-windows//bin//phantomjs.exe")
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
payload={'username':'glxyqx','password':'glxyqx2015'}
theurl='http://twi.xmu.edu.cn/vms/xmuzyz/index.php/login'
driver.get(theurl)
driver.find_element_by_id('username').clear()
driver.find_element_by_id('username').send_keys('glxyqx')
driver.find_element_by_id('passowrd').clear()
driver.find_element_by_id('passowrd').send_keys('glxyqx2015')
driver.find_element_by_tag_name('button').click()
driver.get(web)
na=[]
alltr=driver.find_elements_by_tag_name('tr')
for tr in alltr[1:-1]:
    findd=tr.find_elements_by_tag_name('td')
    na.append([int(findd[1].text),findd[2].text,findd[5].text])
ex=pandas.read_excel(exceladd)
ee=set(ex['学号'])
pt=[['不在报名表上的同学','',''],['学号','姓名','电话']]
tn=na
na=pandas.DataFrame(na)
nas=set(na[0])
kkk=nas.difference(ee)
if(len(kkk)>0):
    for k in list(kkk):
        for i in range(len(tn)):
            if(tn[i][0]==k):
                pt.append(tn[i])
                break
pt.append(['未在系统上报名的同学','',''])
pt.append(['姓名','学号','工时'])
kkks=ee.difference(nas)
if(len(kkks)>0):
    for k in list(kkks):
        for i in range(len(ee)):
            if(list(ex['学号'])[i]==k):
                li=list(ex.iloc[i])
                del li[0]
                del li[-1]
                pt.append(li)
                break
npt=pandas.DataFrame(pt)
npt.to_excel("未报名同学名单.xlsx")
print("已在当前目录生成 未报名同学名单.xlsx")