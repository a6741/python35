# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 22:16:27 2017

@author: hp
"""
starttime='2017-01-01'
endtime='2017-12-31'
actionname=input("请输入想要查询的活动名称，可以是全称也可以是节选\n")
start=starttime.split('-')
syear=start[0]
smonth=start[1]
sday=start[2]
end=endtime.split('-')
eyear=end[0]
emonth=end[1]
eday=end[2]
from selenium import webdriver
driver = webdriver.PhantomJS(executable_path="phantomjs-2.1.1-windows//bin//phantomjs.exe")
theurl='http://twi.xmu.edu.cn/vms/xmuzyz/index.php/login'
driver.get(theurl)
driver.find_element_by_id('username').clear()
driver.find_element_by_id('username').send_keys('')
driver.find_element_by_id('passowrd').clear()
driver.find_element_by_id('passowrd').send_keys('')
driver.find_element_by_tag_name('button').click()
driver.get('http://twi.xmu.edu.cn/vms/xmuzyz/index.php/ytw/index')
x=driver.find_element_by_tag_name("input")
x.clear()
x.send_keys(actionname)
driver.find_element_by_tag_name('button').click()
trs=driver.find_elements_by_tag_name('tr')
le=len(trs)
num=0
gs=0
for tt in range(le-1):
    tr=trs[tt+1]
    time=tr.find_elements_by_tag_name('td')[2].text
    times=time.split('-')
    if(times[0]>eyear or times[0]<syear):
        continue
    if(times[1]>emonth or times[1]<smonth):
        continue
    if(times[2]>eday or times[2]<sday):
        continue
    if(tr.find_elements_by_tag_name('td')[5].text!='通过审核'):
        continue
    newurl=tr.find_elements_by_tag_name('td')[6].find_element_by_tag_name('a').get_attribute('href')
    print(tr.find_elements_by_tag_name('td')[3].find_element_by_tag_name('a').text)
    driver.get(newurl)
    newtrs=driver.find_elements_by_tag_name('tr')
    for ntr in newtrs[1:-1]:
        if(ntr.find_elements_by_tag_name('td')[9].text=='时长审核通过'):
            num+=1
            gs+=float(ntr.find_elements_by_tag_name('td')[8].text)
            print(num)
    driver.get('http://twi.xmu.edu.cn/vms/xmuzyz/index.php/ytw/index')
    x=driver.find_element_by_tag_name("input")
    x.clear()
    x.send_keys(actionname)
    driver.find_element_by_tag_name('button').click()
    trs=driver.find_elements_by_tag_name('tr')
print('人数')
print(num)
print('工时')
print(gs)
