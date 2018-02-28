
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 15:34:40 2017

@author: hp
"""
import time
import codecs
from selenium import webdriver
import os
import socket
def doit(thename,theurl,price,name,visit):
    print('!')
    driver = webdriver.PhantomJS(executable_path="phantomjs-2.1.1-windows//bin//phantomjs.exe")
    driver.set_page_load_timeout(30)
    driver.set_script_timeout(30)
    driver.get(theurl)
    #os.mkdir("C:/Users/hp/Desktop/电子商务大作业/商品信息/"+thename)
    before='<html>\n<head>\n  <title>微商城</title>\n\t<link rel="stylesheet" href="../../../css/style.css" />\n</head>\n<body onLoad="a()">\n<script> function a(){hansu}\n</script>\n<iframe class="goodtop" src="../../../商品顶部.html"></iframe>\n<img src="0.png" class="img5"/>\n<div class="goodstyle">\n<div class="goodinfo">价格：</div>\n<div class="gprice"><strong>{price}</strong></div>\n<div class="goodinfo">月销量：</div>\n<div class="gsale"><strong>{sales}</strong></div>\n<div class="goodinfo">数量：</div>\n<div class="goodinfo">&nbsp;</div>\n<div class="goodinfo">&nbsp;</div>\n<div class="goodinfo">服务承诺：  正品保证   极速退款   七天无理由退换</div>\n</div>\n<br>\n<br>·\n\n<form  action="/../../../../receive.php" method="post">\n<input style="width:30px; height:20px;left:50%; position:absolute; top:71%; border:#000000 outset thin" type="text" name="number" value="1">\n<input style="width:30px; height:20px;left:50%; position:absolute; top:71%; border:#000000 outset thin" type="hidden" name="g_id"  value=>\n<br>\n</form>\n<input style="width:100px; height:50px;left: 60%; position:absolute; top: 81%; color:#FFFFFF; background-color:#FF0000" type="submit" value="加入购物车" >\n<form  action="/../../../../receive2.php" method="post">\n<input style="width:100px; height:50px;left: 50%; position:absolute; top: 81%; color:#FFFFFF; background-color:#FF0000" type="submit" value="现在购买">\n</form>\n<body>\n<div class="info">规格参数<br/>品牌：{brand}<br/>  商品名称:{name}<br/>\n商品编号：{tid}&nbsp;&nbsp;&nbsp;商品毛重：{weight}&nbsp;&nbsp;&nbsp;商品产地：{tfrom}\n</div>\n<div class="xqdiv">\n{spxq}\n</div>\n</body>\n</html>'
    spxq='<img class="xqimg" src="{thexq}.png"/>'
    headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
    import requests ##导入requests
    sales=int(int(visit)*2+int(visit)/10+int(visit)/100)
    cansu=driver.find_element_by_class_name('des_info').find_elements_by_tag_name('dd')
    brand=good=tid=weight=tfrom=''
    for ca in cansu:
        if('品牌' in ca.get_attribute('title')):
            brand=ca.get_attribute('title').replace('品牌：','')
        if('商品名称' in ca.get_attribute('title')):
            good=ca.get_attribute('title').replace('商品名称：','')
        if('商品编号' in ca.get_attribute('title')):
            tid=ca.get_attribute('title').replace('商品编号：','')
        if('商品毛重' in ca.get_attribute('title')):
            weight=ca.get_attribute('title').replace('商品毛重：','')
        if('商品产地' in ca.get_attribute('title')):
            tfrom=ca.get_attribute('title').replace('商品产地：','')
    driver.find_element_by_class_name('desbox').click()
    ww=driver.find_element_by_class_name('desbox').find_elements_by_tag_name('img')
    i=1
    sp=''
    for w in ww:
      try:
        imghref=w.get_attribute('src')
        img = requests.get(imghref, headers=headers)   
        f = open("C:/Users/hp/Desktop/dszy/spxx/"+thename+'/'+str(i)+'.png', 'ab')##写入多媒体文件必须要 b 这个参数！！必须要！！
        f.write(img.content) ##多媒体文件要是用conctent哦！
        f.close()
        sp+=spxq.format(thexq=str(i))
        i+=1
      except:  
          pass
    be=before.format(name=name,price=price,sales=sales,brand=brand,tid=tid,weight=weight,tfrom=tfrom,spxq=sp,hansu="\n document.getElementsByTagName(\'input\')[1].value=document.getElementsByClassName(\'info\')[0].innerHTML.split(\'<br>\')[3].split(\'&\')[0].split(\'：\')[1];")
    f = codecs.open("C:/Users/hp/Desktop/dszy/spxx/"+thename+"/good.html", "w", "utf-8")
    f.write(be)
    f.close()
    driver.quit()
    return True