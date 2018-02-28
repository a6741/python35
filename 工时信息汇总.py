# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 22:16:27 2017

@author: hp
"""
starttime="2017-01-01"
endtime="2017-12-29"
actionname="迎新"
import pandas
from selenium import webdriver
driver = webdriver.PhantomJS(executable_path="phantomjs-2.1.1-windows//bin//phantomjs.exe")
theurl='http://twi.xmu.edu.cn/vms/xmuzyz/index.php/login'
driver.get(theurl)
driver.find_element_by_id('username').clear()
driver.find_element_by_id('username').send_keys('')
driver.find_element_by_id('passowrd').clear()
driver.find_element_by_id('passowrd').send_keys('')
driver.find_element_by_tag_name('button').click()
driver.get('http://twi.xmu.edu.cn/vms/xmuzyz/index.php/ytw/index4')
x=driver.find_element_by_name("qishinianji")
x.find_element_by_xpath("//*[@id='main']/div[2]/form/div[1]/select/option[11]").click()
kk=driver.find_elements_by_id("hdsj")[1]
kk.clear()
kk.send_keys(starttime)
yy=driver.find_elements_by_id("jssj")[1]
yy.clear()
yy.send_keys(endtime)
driver.find_elements_by_tag_name('button')[1].click()
alltr=driver.find_elements_by_tag_name('tr')
#(['姓名','年级','活动','时长'])
na=[]
for tr in alltr:
    try:
        info=tr.find_elements_by_tag_name('td')
        if(actionname in info[4].text):
            print("正在录入")
            na.append([info[1].text,info[2].text,info[4].text,info[5].text])
    except:
        pass
na=pandas.DataFrame(na)
all=0
for k in na[3]:
    all+=float(k)
print(str(len(na.drop_duplicates([0])))+'个人'+str(all)+'工时')
input('输入任意键退出')
