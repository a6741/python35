# -*- coding: utf-8 -*-%
"""
Created on Tue Sep 19 21:12:57 2017

@author: hp
"""


import itchat
list=['/微笑','/撇嘴','/吐','/再见','/难过','/刀','/发抖','/抱拳','/抠鼻']
i=0
global list,i
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    global list,i
    i=(i+2)%9
    itchat.send(msg['Text']+list[i],msg['FromUserName'])

itchat.auto_login()
itchat.run()