# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 18:25:20 2017

@author: hp
"""
from PIL import Image
import os
import requests 
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import itchat
def getip():
    global headers
    proxys=[]
    global ips
    ips=[]
    url = 'http://www.xicidaili.com/nn/1'
    shtml=requests.get(url,headers=headers)
    Soup=BeautifulSoup(shtml.text,'lxml')
    if 'block' in Soup:
        print('fuck')
    theurl=Soup.find_all('tr',class_="odd")
    for ur in theurl:
        proxys.append({ur.find_all('td')[5].get_text().lower(): "http://"+ur.find_all('td')[1].get_text()+":"+ur.find_all('td')[2].get_text()})
    url = "http://ip.chinaz.com/getip.aspx"
    for proxy in proxys:
        if len(ips)>=15:
            break
        try:
            res = requests.get(url,proxies=proxy)
            so=BeautifulSoup(res.text,'lxml')
            print(so.get_text())
            ips.append(proxy)
        except:
            continue
def getwx(c):
    global thetex,headers,ipnum,ips,theimg
    print('开始爬取 '+c)
    #time.sleep(1)
    all_url='http://weixin.sogou.com/weixin?type=1&s_from=input&query='+c+'&ie=utf8&_sug_=n&_sug_type_='
    shtml=requests.get(all_url,headers=headers)
    Soup=BeautifulSoup(shtml.text,'lxml')
    try:
        theurl=Soup.find('p',class_='tit').find('a',target='_blank')['href']
    except:
        print('对不起，搜狗微信上无法查询到此公众号')
        return 'ok'
    '''
    proxy=webdriver.Proxy()
    #proxy.proxy_type=ProxyType.MANUAL
    proxy.http_proxy=str(ips[ipnum].values()).replace("'])",'').split('//')[1]
    # 将代理设置添加到webdriver.DesiredCapabilities.PHANTOMJS中
    proxy.add_to_capabilities(webdriver.DesiredCapabilities.PHANTOMJS)
    driver = webdriver.PhantomJS(executable_path="D://phantomjs-2.1.1-windows//bin//phantomjs.exe")
    '''
    driver.get(theurl)
    #cookie = driver.get_cookies()
   # global cookie
    #driver.add_cookie(cookie)
    #driver.delete_cookie()
    time.sleep(1)
    global a
    a=driver.page_source
    trytime=0
    while '验证码' in a:#关于验证码问题目前还没有好的对策，试过改ip但没有用，图像识别目前我还不太懂
        #print('点击过于频繁，网站需要输入验证码,请进入\n'+theurl+'\n输入验证码后重新启动程序\n或者减少一次需要爬取的公众号数量')
        #
        if trytime>5:
            print("可能是被网站封了，过几天再运行吧...")
            return 'no'
        driver.save_screenshot('验证码页面.png')
        element=driver.find_element_by_id('verify_img')
        #location办法可能会有偏移，但是每次都会锁定了了验证码的位置，所以稍微修正一下location的定位，后面都管用
        left   = element.location['x']#验证码图片左上角横坐标
        top    = element.location['y']#验证码图片左上角纵坐标
        right  = left + element.size['width']#验证码图片右下角横坐标
        bottom = top + element.size['height']#验证码图片右下角纵坐标
        im=Image.open('验证码页面.png')
        im_crop=im.crop((left,top,right,bottom))
        im_crop.show()
        driver.find_element_by_id('input').send_keys(input('输入图中验证码:'))
        driver.find_element_by_id('bt').click()
        time.sleep(2)
        a=driver.page_source
        os.remove('验证码页面.png')
        trytime+=1
        #
        '''ipnum+=1
        if ipnum>=len(ips):
            return 'fuck'
        driver.delete_all_cookies()
        driver.close()
        getwx(c)'''
        #注释掉的是原本打算通过换ip来绕过验证码，但似乎并没有用
        #return('no')#####
    global ac
    ac=len(driver.find_elements_by_tag_name('h4'))
    if ac==0:
        #print(a)
        print('点击过于频繁，网站需要输入验证码,请进入\n'+theurl+'\n输入验证码后重新启动程序\n或者减少一次需要爬取的公众号数量')
        return 'no'
    for i in range(ac):
        try:
            driver.find_elements_by_tag_name('h4')[i].click()
            time.sleep(2)#等待图片加载
            driver.save_screenshot(str(len(thetex))+'.png')
            thetex[len(thetex)+'.png']=driver.find_element_by_xpath("html").text
            print("it is the"+driver.title)
        except:
            a=driver.page_source
            trytime=0
            while '验证码' in a:#关于验证码问题目前还没有好的对策，试过改ip但没有用，图像识别目前我还不太懂
                #print('点击过于频繁，网站需要输入验证码,请进入\n'+theurl+'\n输入验证码后重新启动程序\n或者减少一次需要爬取的公众号数量')
                #
                if trytime>5:
                    print("可能是被网站封了，过几天再运行吧...")
                    return 'no'
                driver.save_screenshot('验证码页面.png')
                element=driver.find_element_by_id('verify_img')                    #location办法可能会有偏移，但是每次都会锁定了了验证码的位置，所以稍微修正一下location的定位，后面都管用
                left   = element.location['x']#验证码图片左上角横坐标
                top    = element.location['y']#验证码图片左上角纵坐标
                right  = left + element.size['width']#验证码图片右下角横坐标
                bottom = top + element.size['height']#验证码图片右下角纵坐标
                im=Image.open('验证码页面.png')
                im_crop=im.crop((left,top,right,bottom))
                im_crop.show()
                driver.find_element_by_id('input').send_keys(input('输入图中验证码:'))
                driver.find_element_by_id('bt').click()
                time.sleep(2)
                a=driver.page_source
                os.remove('验证码页面.png')
                trytime+=1
                #
                '''ipnum+=1
                if ipnum>=len(ips):
                    return 'fuck'
                driver.delete_all_cookies()
                driver.close()
                getwx(c)'''
                #注释掉的是原本打算通过换ip来绕过验证码，但似乎并没有用
                #return('no')#####
            if (driver.title==c):
                driver.find_elements_by_tag_name('h4')[i].click()
                time.sleep(2)
                driver.save_screenshot(str(len(thetex))+'.png')
                thetex[str(len(thetex))+'.png']=driver.find_element_by_xpath("html").text
            else:
                driver.save_screenshot(str(len(thetex))+'.png')
                thetex[str(len(thetex))+'.png']=driver.find_element_by_xpath("html").text
 
            print(driver.title)
                
            driver.back()
    print('爬取 '+c+' 结束')
    #driver.delete_cookie()
    return 'ok'
def send(names):
    global thetex
    user= itchat.search_friends(name=names)[0]
    #找到UserName
    userName = user['UserName']
    #然后给他发消息
    for i in thetex:
        trys=0
        itchat.send(thetex[i],toUserName = userName)
        while "'Ret': 1" in str(itchat.send_image(fileDir=i,toUserName = userName)):
            trys+=1
            if(trys>10):
                itchat.send('截图发送失败',toUserName = userName)
                break
        print(i)
        os.remove(i)
if __name__ == "__main__":
    global thetex,headers,ipnum
    ipnum=0
    thetex={}
    headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
    itchat.login()
    driver = webdriver.PhantomJS(executable_path="D://phantomjs-2.1.1-windows//bin//phantomjs.exe")#需要下载phantomjs并填入其执行路径
    #print('一般来说每天第一次运行一次能爬取48篇左右，然后就会出验证码，之后篇数越来越少')
    #getip()#获取代理ip
    mpsList=itchat.get_mps(update=True)[0:]
    want=input('输入公众号名称:\n')
    for i in mpsList:
        if want in i['NickName']:
            if 'no'==getwx(i['NickName']):
                ok=0
                break
            else:
                ok=1
    if(ok==1):
        print('*****爬取成功****')
    else:
        print('爬取失败或未全部爬取完')
    friends = itchat.get_friends(update=True)[0:]
    sendto=input('输入要发送的好友:\n')
    send(sendto)