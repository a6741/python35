# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 15:34:40 2017

@author: hp
"""
import codecs
import time
from selenium import webdriver
import os
def makeit(thename,theurl):
    path='C:/Users/hp/Desktop/电子商务大作业/商品信息/'+thename
    os.mkdir(path)
    txt=""
    tt=1
    before='<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n<html xmlns="http://www.w3.org/1999/xhtml">\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n<title>微商城</title>\n<link rel="stylesheet" href="css/style.css" />\n<script type="text/javascript" src="js/jquery-1.9.1.min.js"></script>\n<script type="text/javascript" src="js/jquery.min.js"></script>\n<script type="text/javascript" src="js/style.js" ></script>\n<style type="text/css">\n*{margin:0;padding:0;list-style-type:none;}\nbody{ background-image:url(1.png)}\na,img{border:none;}\n\n.zx_slider\n{position:relative;\nmargin:40px auto 0 auto;\nwidth:1002px;\nheight:350px;\noverflow:hidden;\nborder-radius:5px;}\n.zx_slider .imgbox\n{width:3750px;\nheight:310px;\nposition:absolute;\nleft:5px;\ntop:4px;}\n.zx_slider .imgbox img\n{float:left;\nwidth:750px;\nheight:310px;}\n.zx_slider .png\n{width:1002px;\nheight:350px;\nleft:0px;\ntop:0px;\nposition:absolute;\nbackground:url(../jquery-hor-thumb-slider/jquery-hor-thumb-slider/img/slider_bg.png);\n_background:none;\nfilter:progid:DXImageTransform.Microsoft.AlphaImageLoader(src="img/slider_bg.png");}\n.zx_slider .lbtn\n{cursor:pointer;\nwidth:45px;\nheight:55px;\nposition:absolute;\nleft:0px;bottom:-3px;\nbackground:url(../jquery-hor-thumb-slider/jquery-hor-thumb-slider/img/slider_l_btn.png);\n_background:none;\nfilter:progid:DXImageTransform.Microsoft.AlphaImageLoader(src="img/slider_l_btn.png");}\n.zx_slider .rbtn\n{cursor:pointer;\nwidth:45px;height:55px;\nposition:absolute;\nleft:718px;\nbottom:-3px;\nbackground:url(../jquery-hor-thumb-slider/jquery-hor-thumb-slider/img/slider_r_btn.png);\n_background:none;\nfilter:progid:DXImageTransform.Microsoft.AlphaImageLoader(src="img/slider_r_btn.png");}\n.zx_slider .btnbox\n{width:750px;\nheight:60px;\nposition:absolute;\nleft:30px;\nbottom:0px;}\n.zx_slider .btnbox a\n{cursor:pointer;\ndisplay:inline-block;\nfloat:left;\nwidth:126px;\nheight:54px;\nmargin:0 0 0 10px;}\n.zx_slider .btnbox a img\n{position:relative;\ndisplay:inline;\nwidth:120px;\nheight:48px;\nfloat:left;\nborder:3px solid #392101;\nborder-radius:2px;}\n.zx_slider .btnbox a .img_hover\n{border:3px solid #e4471f;\nborder-radius:2px;}\n.zx_slider .slider_p\n{overflow:hidden;\nwidth:220px;height:290px;\nposition:absolute;right:15px;top:15px;}\n.zx_slider .slider_p h3{margin:20px 0 10px 0;font-size:20px;text-align:center;color:#faa629;}\n.zx_slider .slider_p p{line-height:26px;font-size:14px;color:#faa629;}\n.hi_btn{width:740px;height:330px;position:absolute;left:0px;top:0px;display:block;}\n.mainframe{\nposition:absolute;\nleft:5%;\ntop:80%;\nwidth:78%;\n}\n.mainpanel{\nfont-size:24px;\nposition:relative;\nleft:20%;\ntop:0%;\nwidth:70%;\n}\n.goods{\nfloat:left;\nfont-size:20px;\nposition:relative;\nleft:20%;\ntop:10%;\nwidth:22%;\n}\n.goodsimg{\nposition:relative;\nwidth:100%;\nleft:0%;\ntop:0%;\n}\n.block{\nfloat:left;\nposition:relative;\nleft:20%;\ntop:0%;\nwidth:3%;\n}\n.pont2{\nposition:absolute;\n z-index:2;\n  left:94%;\n   top:15%;\n    color:#FFFFFF;\n\t font-size:48px;\n\t  font:\'微软雅黑\';\n}\n</style>\n\n</head>\n\n<body>\n\n<div class="zx_slider">\n\n    <div class="imgbox">\n        <img alt="Danx" src="img/danx1.jpg" width="750" height="310" />\n        <img alt="Danx" src="img/danx2.jpg" width="750" height="310" />\n        <img alt="Danx" src="img/danx3.jpg" width="750" height="310" />\n        <img alt="Danx" src="img/danx4.jpg" width="750" height="310" />\n        <img alt="Danx" src="img/danx5.jpg" width="750" height="310" />\n    </div>\n\n    <div class="png"></div>\n\n    <a href="#" id="hi_btn0" class="hi_btn"></a>\n    <a href="#" id="hi_btn1" class="hi_btn"></a>\n    <a href="#" id="hi_btn2" class="hi_btn"></a>\n    <a href="#" id="hi_btn3" class="hi_btn"></a>\n    <a href="#" id="hi_btn4" class="hi_btn"></a>\n\n    <div class="btnbox">\n        <a onmouseover="btn_m_over(0)"><img alt="Danx" id="btn_img0" class="thumb img_hover" src="img/danx1.jpg" /></a>\n        <a onmouseover="btn_m_over(1)"><img alt="Danx" id="btn_img1" class="thumb" src="img/danx2.jpg" /></a>\n        <a onmouseover="btn_m_over(2)"><img alt="Danx" id="btn_img2" class="thumb" src="img/danx3.jpg" /></a>\n        <a onmouseover="btn_m_over(3)"><img alt="Danx" id="btn_img3" class="thumb" src="img/danx4.jpg" /></a>\n        <a onmouseover="btn_m_over(4)"><img alt="Danx" id="btn_img4" class="thumb" src="img/danx5.jpg" /></a>\n    </div>\n\n    <div class="lbtn"></div>\n    <div class="rbtn"></div>\n\n    <div class="slider_p">\n\n        <div id="slider_p0" class="slider_p_div">\n\t\t\t<h3>标题1</h3>\n\t\t\t<p>百度（Nasdaq简称：BIDU）是全球最大的中文搜索引擎，2000年1月由李彦宏、徐勇两人创立于北京中关村，致力于向人们提供“简单，可依赖”的信息获取方式。“百度”二字源于中国宋朝词人辛弃疾的《青玉案·元夕》词句“众里寻他千百度”，象征着百度对中文信息检索技术的执著追求。</p>\n        </div>\n\n        <div id="slider_p1" class="slider_p_div">\n\t\t\t<h3>标题2</h3>\n\t\t\t<p>2000年1月由李彦宏、徐勇两人创立于北京中关村，致力于向人们提供“简单，可依赖”的信息获取方式。“百度”二字源于中国宋朝词人辛弃疾的《青玉案·元夕》词句“众里寻他千百度”，象征着百度对中文信息检索技术的执著追求。</p>\n        </div>\n\n        <div id="slider_p2" class="slider_p_div">\n\t\t\t<h3>标题3</h3>\n\t\t\t<p>致力于向人们提供“简单，可依赖”的信息获取方式。“百度”二字源于中国宋朝词人辛弃疾的《青玉案·元夕》词句“众里寻他千百度”，象征着百度对中文信息检索技术的</p>\n        </div>\n\n        <div id="slider_p3" class="slider_p_div">\n\t\t\t<h3>标题4</h3>\n\t\t\t<p>您到卡上黑暗圣经卡萨丁</p>\n        </div>\n\n        <div id="slider_p4" class="slider_p_div">\n\t\t\t<h3>标题5</h3>\n\t\t\t<p>打考勤卡和饭来欺骗卡号发</p>\n        </div>\n\n    </div>\n\n</div><!--zx_slider end-->\n<input style="position:absolute; left:15%; top:70%; height:3%; width:50%" type="text" id="bar1" onMouseOut="f()"/>\n<button name="搜索" style=" position:absolute;left:68%; top:69.8%; width:5%; height:4%; background-color:#0066CC; color:#FFFFFF">搜索</button>'
    txt=before
    kk="<div class='goods'><img class='goodsimg' src='{0}' />{1}<br />仅售<b>{2}</b></div><div class='block'>&nbsp;</div>"
    headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
    import requests ##导入requests
    driver = webdriver.PhantomJS(executable_path="phantomjs-2.1.1-windows//bin//phantomjs.exe")
    theurl='http://search.yhd.com/c0-0-1004989/'
    driver.get(theurl)
    alls=driver.find_elements_by_class_name('itemBox')
    for al in alls[1:]:
        img_url=al.find_element_by_tag_name('img').get_attribute('src')
        try:
            name=al.find_element_by_class_name('mainTitle').get_attribute('title')
            price=al.find_element_by_class_name('num').text
            img = requests.get(img_url, headers=headers)
            f = open(path+'/'+name.replace(' ','').replace('*','')+'.png', 'ab')##写入多媒体文件必须要 b 这个参数！！必须要！！
            f.write(img.content) ##多媒体文件要是用conctent哦！
            f.close()
            kkk=kk.format('商品信息/yue/'+name.replace(' ','').replace('*','')+'.png',name,price)
            txt+=kkk
            txt+="\n"
            if(tt%5==0):
                txt+="<div class='longblock'>&nbsp;</div>\n"
                print('!')
            tt+=1
            if(tt>20):
                break
            print(name)
        except:
            pass
    txt+='\n<script type="text/javascript">\nvar slider_count=4;\n$(".slider_p_div").hide();\n$("#slider_p0").show();\n$(".hi_btn").hide();\n$("#hi_btn0").show();\n$(".img_hover").animate({bottom:"10px"});\nvar slider_i=1;\nvar m_over=true;\nfunction f()\n{\nvar kuang1 = document.getElementById("bar1")\n}\nfunction zx_slider(){\n	if(m_over){\n		if(slider_i<0){slider_i=slider_count;}\n		//p\n		$(".slider_p_div").hide();\n		$("#slider_p"+slider_i).show();\n		//p end\n		//hi_btn\n		$(".hi_btn").hide();\n		$("#hi_btn"+slider_i).show();\n		//hi_btn end\n		//btn\n		$(".btnbox img").stop(true,true);\n		$(".btnbox img").removeClass("img_hover");\n		$(".btnbox img").animate({bottom:"0px"},200);\n		$("#btn_img"+slider_i).addClass("img_hover");\n		$("#btn_img"+slider_i).animate({bottom:"10px"},200);\n		//btn end\n		$(".imgbox").stop();\n		$(".imgbox").animate({left:"-750"*slider_i+"px"});\n		if(slider_i<slider_count){\n			slider_i++;	\n		}else{\n			slider_i=0;\n		}\n	}\n}\n$(".lbtn").click(function(){\n	m_over=true;\n	if(slider_i==0){slider_i=slider_count-1}else{slider_i=slider_i-2;}\n	zx_slider();\n	m_over=false;\n});\n\n$(".rbtn").click(function(){\n	m_over=true;\n	zx_slider();\n	m_over=false;\n});\n\nfunction btn_m_over(btn_i){\n	if(slider_i-1!=btn_i){\n		m_over=true;\n		slider_i=btn_i;\n		zx_slider();\n		m_over=false;\n	}\n}\n\nzx_timer=setInterval("zx_slider();",5000); \n$(".zx_slider").mouseover(function(){\n	m_over=false;\n});\n$(".zx_slider").mouseout(function(){\n	m_over=true;\n});\n</script>\n\n<div style="text-align:center;clear:both">\n<script src="/gg_bd_ad_720x90.js" type="text/javascript"></script>\n<script src="/follow.js" type="text/javascript"></script>\n</div>\n</body>\n</html>\n'
    f = codecs.open("C:/Users/hp/Desktop/电子商务大作业/"+thename+".html", "w", "utf-8")
    f.write(txt)
    f.close()
