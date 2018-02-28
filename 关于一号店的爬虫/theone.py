# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 15:34:40 2017

@author: hp
"""
import goods
import codecs
from selenium import webdriver
import os
def makeit(thename,theurl,theid):
    path='C:/Users/hp/Desktop/dszy/spxx/'+theid        
    sqlt=''
    sq='insert into goods values({});\n'
    txt=""
    tt=1
    before='<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n<html xmlns="http://www.w3.org/1999/xhtml">\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n<title>微商城</title>\n<link rel="stylesheet" href="css/style.css" />\n<script type="text/javascript" src="js/jquery-1.9.1.min.js"></script>\n<script type="text/javascript" src="js/jquery.min.js"></script>\n<script type="text/javascript" src="js/style.js" ></script>\n<script type="text/javascript" src="js/slide.js" ></script>\n</head>\n<body>\n<div>\n <iframe src="主页.html" frameborder="0" scrolling="no" class="mainframe2">\n 您的浏览器不支持iframe，请升级\n </iframe>\n</div>\n<div class="mainframe">'
    txt=before
    kk="<div class='goods'><img class='goodsimg' src='{0}' /><a class='spxq' href='{1}'>{2}<a/><br />仅售<b>{3}</b></div><div class='block'>&nbsp;</div>"
    headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
    import requests ##导入requests
    driver = webdriver.PhantomJS(executable_path="phantomjs-2.1.1-windows//bin//phantomjs.exe")
    driver.set_page_load_timeout(30)
    driver.set_script_timeout(30)
    driver.get(theurl)
    alls=driver.find_elements_by_class_name('itemBox')
    for al in alls[1:]:
        img_url=al.find_element_by_tag_name('img').get_attribute('src')
        try:
            name=al.find_element_by_class_name('mainTitle').get_attribute('title')
            price=al.find_element_by_class_name('num').text
            visit=al.find_element_by_class_name('comment').find_element_by_tag_name('a').get_attribute('experiencecount')
            if visit=='':
                visit=0
            img = requests.get(img_url, headers=headers)
            goodhref=al.find_element_by_class_name('img').get_attribute('href')
            filename=name.replace(' ','').replace('*','')        
            tid=al.find_element_by_class_name('img').get_attribute('id').split('_')[-1]     
            os.mkdir("C:/Users/hp/Desktop/dszy/spxx/"+theid+'/'+tid)
            goods.doit(theid+'/'+tid,goodhref,price,name,visit)
            f = open(path+'/'+tid+'/0.png', 'ab')##写入多媒体文件必须要 b 这个参数！！必须要！！
            f.write(img.content) ##多媒体文件要是用conctent哦！
            f.close()
            kkk=kk.format('spxx/'+theid+'/'+tid+'/0.png','spxx/'+theid+'/'+tid+"/good.html",name,price)
            txt+=kkk
            txt+="\n"
            sqlt+=sq.format(tid+','+price.replace("¥",'')+',"'+thename+'","'+filename+'"')
            if(tt%5==0):
                txt+="<div class='longblock'>&nbsp;</div>\n"
                print('!')
            tt+=1
            if(tt>20):
                break
            print(name)
        except:
            pass
    txt+='<script type="text/javascript">\nvar slider_count=4;\n$(".slider_p_div").hide();\n$("#slider_p0").show();\n$(".hi_btn").hide();\n$("#hi_btn0").show();\n$(".img_hover").animate({bottom:\'10px\'});\nvar slider_i=1;\nvar m_over=true;\nfunction zx_slider(){\n\tif(m_over){\n\t\tif(slider_i<0){slider_i=slider_count;}\n\t\t//p\n\t\t$(".slider_p_div").hide();\n\t\t$("#slider_p"+slider_i).show();\n\t\t//p end\n\t\t//hi_btn\n\t\t$(".hi_btn").hide();\n\t\t$("#hi_btn"+slider_i).show();\n\t\t//hi_btn end\n\t\t//btn\n\t\t$(".btnbox img").stop(true,true);\n\t\t$(".btnbox img").removeClass("img_hover");\n\t\t$(".btnbox img").animate({bottom:\'0px\'},200);\n\t\t$("#btn_img"+slider_i).addClass("img_hover");\n\t\t$("#btn_img"+slider_i).animate({bottom:\'10px\'},200);\n\t\t//btn end\n\t\t$(".imgbox").stop();\n\t\t$(".imgbox").animate({left:\'-750\'*slider_i+\'px\'});\n\t\tif(slider_i<slider_count){\n\t\t\tslider_i++;\t\n\t\t}else{\n\t\t\tslider_i=0;\n\t\t}\n\t}\n}\n$(".lbtn").click(function(){\n\tm_over=true;\n\tif(slider_i==0){slider_i=slider_count-1}else{slider_i=slider_i-2;}\n\tzx_slider();\n\tm_over=false;\n});\n\n$(".rbtn").click(function(){\n\tm_over=true;\n\tzx_slider();\n\tm_over=false;\n});\n\nfunction btn_m_over(btn_i){\n\tif(slider_i-1!=btn_i){\n\t\tm_over=true;\n\t\tslider_i=btn_i;\n\t\tzx_slider();\n\t\tm_over=false;\n\t}\n}\n\nzx_timer=setInterval("zx_slider();",5000); \n$(".zx_slider").mouseover(function(){\n\tm_over=false;\n});\n$(".zx_slider").mouseout(function(){\n\tm_over=true;\n});\n</script>\n</body>\n</html>'
    #f = codecs.open("C:/Users/hp/Desktop/dszy/"+thename+".html", "w", "utf-8")
    #f.write(txt)
    #f.close()
    driver.quit()
    return sqlt
makeit('单反相机','//search.yhd.com/c0-0-1004276/','1461')