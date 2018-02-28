# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 08:15:07 2018

@author: hp
"""

import os
import re
path=r'I:'
for filename in os.listdir(path):  # 获取path下所有文件的路径
    houzui=filename.split('.')[-1]
    newname=''.join(re.findall('[^\x00-\xff]',filename))
    if(len(newname)>0):
        while(os.path.exists(path+'\\'+newname+'.'+houzui)):
            newname+='-'
        os.rename(path+'\\'+filename,path+'\\'+newname+'.'+houzui)