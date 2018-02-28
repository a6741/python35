# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 22:16:27 2017

@author: hp
"""
import theone
import codecs
import time
import socket
from selenium import webdriver
path='C:/Users/hp/Desktop/dszy/'
maintxt=''
before='<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n<html xmlns="http://www.w3.org/1999/xhtml">\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n<title>微商城</title>\n<link rel="stylesheet" href="css/style.css" />\n<script type="text/javascript" src="js/jquery-1.9.1.min.js"></script>\n<script type="text/javascript" src="js/jquery.min.js"></script>\n<script type="text/javascript" src="js/style.js" ></script>\n<script type="text/javascript" src="js/slide.js" ></script>\n</head>\n<body>\n<img class="img1" src="main/1.jpg" />\n<input class="input1" type="text" id="bar1"/>\n<button name="搜索"  class="button1" onclick="f()">搜索</button>\n<a class="person" href="个人信息.html" target="_top">查看个人信息</a>\n<a class="thegwc" href="购物车.html" target="_top">购物车</a>'
kt='<div class="containor">\n<div class="nav_left">\n<ul>\n{what}\n</ul>\n</div>\n<div class="nav_right">\n'
kk='<dl>\n<dt><a >{0} <i> &gt;</i></a> </dt>\n<dd>\n{1}</dd>\n</dl>\n'
ks=''
driver = webdriver.PhantomJS(executable_path="phantomjs-2.1.1-windows//bin//phantomjs.exe")
theurl='http://www.yhd.com'
driver.set_page_load_timeout(30)
driver.set_script_timeout(30)
driver.get(theurl)
sql=''
tt=driver.page_source
cla=driver.find_element_by_class_name('hd_more_allsort')
clas=cla.find_elements_by_tag_name('li')
thelen=len(clas)
for le in range(2,thelen-3):
    webdriver.ActionChains(driver).move_to_element(clas[le]).perform()
    time.sleep(5)
    tt=driver.page_source
    cl=clas[le]
    names=cl.find_element_by_tag_name('h3').find_elements_by_tag_name('a')
    name=''
    for na in names:
        if(len(name)!=0):
            name+='/'
        name+=na.text
    dts=cl.find_elements_by_class_name('clearfix')
    maintxt+='<div class="sub hide" data-id="'+str(le)+'">\n'
    for dt in dts[1:8]:
        try:
            aa=dt.find_elements_by_tag_name('a')
            mainname=aa[0].text
            ww=''
            for a in aa[1:10]:
                thehref=a.get_attribute('href')
                sqsq=theone.makeit(a.text,thehref,a.get_attribute('categoryid'))
                if(sqsq!=''):
                    ww+='<a href="'+a.text+'.html" target="_top">'+a.text+'</a>\n'
                    sql+='insert into type values('+a.get_attribute("categoryid")+',"'+a.text+'");\n'
            maintxt+=kk.format(mainname,ww)
        except:
            pass
    maintxt+='</div>\n'
    ks+='<li data-id="'+str(le)+'"> <span>'+name+'</span></li>\n'
    print('***************')

ass=before
ass+=kt.format(what=ks)
ass+=maintxt
ass+='\n</div>\n</div>'
#一长串js代码
ass+='</div>\n</div><div class="zx_slider">\n\n    <div class="imgbox">\n        <a href="多肉植物.html" target="_top"><img alt="Danx" src="img/danx1.jpg" width="750" height="310" /></a>\n        <a href="单反相机.html" target="_top"><img alt="Danx" src="img/danx2.jpg" width="750" height="310" /></a>\n        <a href="帆布鞋.html" target="_top"><img alt="Danx" src="img/danx3.jpg" width="750" height="310" /></a>\n        <a href="自行车.html" target="_top"><img alt="Danx" src="img/danx4.jpg" width="750" height="310" /></a>\n        <a href="耳机及耳麦.html" target="_top"><img alt="Danx" src="img/danx5.jpg" width="750" height="310" /></a>\n    </div>\n\n\n    <a href="#" id="hi_btn0" class="hi_btn"></a>\n    <a href="#" id="hi_btn1" class="hi_btn"></a>\n    <a href="#" id="hi_btn2" class="hi_btn"></a>\n    <a href="#" id="hi_btn3" class="hi_btn"></a>\n    <a href="#" id="hi_btn4" class="hi_btn"></a>\n\n    <div class="btnbox">\n        <a onmouseover="btn_m_over(0)"><img alt="Danx" id="btn_img0" class="thumb img_hover" src="img/danx1.jpg"/></a>\n        <a onmouseover="btn_m_over(1)"><img alt="Danx" id="btn_img1" class="thumb" src="img/danx2.jpg" /></a>\n        <a onmouseover="btn_m_over(2)"><img alt="Danx" id="btn_img2" class="thumb" src="img/danx3.jpg" /></a>\n        <a onmouseover="btn_m_over(3)"><img alt="Danx" id="btn_img3" class="thumb" src="img/danx4.jpg" /></a>\n        <a onmouseover="btn_m_over(4)"><img alt="Danx" id="btn_img4" class="thumb" src="img/danx5.jpg" /></a>\n    </div>\n    <div class="lbtn"></div>\n    <div class="rbtn"></div>\n</div><!--zx_slider end-->\n<script type="text/javascript">\nvar slider_count=4;\n$(".slider_p_div").hide();\n$("#slider_p0").show();\n$(".hi_btn").hide();\n$("#hi_btn0").show();\n$(".img_hover").animate({bottom:\'10px\'});\nvar slider_i=1;\nvar m_over=true;\nfunction zx_slider(){\n\tif(m_over){\n\t\tif(slider_i<0){slider_i=slider_count;}\n\t\t//p\n\t\t$(".slider_p_div").hide();\n\t\t$("#slider_p"+slider_i).show();\n\t\t//p end\n\t\t//hi_btn\n\t\t$(".hi_btn").hide();\n\t\t$("#hi_btn"+slider_i).show();\n\t\t//hi_btn end\n\t\t//btn\n\t\t$(".btnbox img").stop(true,true);\n\t\t$(".btnbox img").removeClass("img_hover");\n\t\t$(".btnbox img").animate({bottom:\'0px\'},200);\n\t\t$("#btn_img"+slider_i).addClass("img_hover");\n\t\t$("#btn_img"+slider_i).animate({bottom:\'10px\'},200);\n\t\t//btn end\n\t\t$(".imgbox").stop();\n\t\t$(".imgbox").animate({left:\'-750\'*slider_i+\'px\'});\n\t\tif(slider_i<slider_count){\n\t\t\tslider_i++;\t\n\t\t}else{\n\t\t\tslider_i=0;\n\t\t}\n\t}\n}\n$(".lbtn").click(function(){\n\tm_over=true;\n\tif(slider_i==0){slider_i=slider_count-1}else{slider_i=slider_i-2;}\n\tzx_slider();\n\tm_over=false;\n});\n\n$(".rbtn").click(function(){\n\tm_over=true;\n\tzx_slider();\n\tm_over=false;\n});\n\nfunction btn_m_over(btn_i){\n\tif(slider_i-1!=btn_i){\n\t\tm_over=true;\n\t\tslider_i=btn_i;\n\t\tzx_slider();\n\t\tm_over=false;\n\t}\n}\n\nzx_timer=setInterval("zx_slider();",5000); \n$(".zx_slider").mouseover(function(){\n\tm_over=false;\n});\n$(".zx_slider").mouseout(function(){\n\tm_over=true;\n});\n</script>\n</body>\n</html>'
#f = codecs.open(path+"主页.html", "w", "utf-8")
#f.write(ass)
#f.close()
#f = codecs.open(path+"ssql.txt", "w", "utf-8")
#f.write(sql)
#f.close()
driver.quit()