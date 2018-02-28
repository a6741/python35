# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 17:16:30 2018

@author: hp
"""
import tensorflow as tf  

W = tf.Variable([[1,1,1],[2,2,2]],dtype = tf.float32,name='w')  
b = tf.Variable([[0,1,2]],dtype = tf.float32,name='b')  

init = tf.global_variables_initializer()  
saver = tf.train.Saver()  
with tf.Session() as sess:  
        sess.run(init)  
        save_path = saver.save(sess,"save/model.ckpt")  