# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 15:01:27 2017

@author: hp
"""
import PIL.Image as Image
import pytesseract
image = Image.open('2.jpg')  # Open image object using PIL  
k=pytesseract.image_to_string(image)