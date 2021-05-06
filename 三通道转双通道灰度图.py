# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 15:32:55 2021

@author: Alex
"""

import cv2
import numpy as np
import os

def convert(input_dir, output_dir):
    i=1
    for filename in os.listdir(input_dir):
        path = input_dir + "/" + filename # 
        print("processing... ", path)
        color_img = cv2.imread(path)#
        gray_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)
        
        new_name= "gray"+" ("+str(i)+").png"
        cv2.imwrite(output_dir+'/'+filename,gray_img )




if __name__ == '__main__':
    input_dir = r"C:\Users\Alex\Desktop\499 project\数据集处理\JEPG"  
    output_dir = r"C:\Users\Alex\Desktop\499 project\数据集处理\JEPG" 
    convert(input_dir, output_dir)

