# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 15:32:55 2021

@author: Alex
"""

import cv2
import numpy as np
import os

def convert(input_dir, output_dir):
    for filename in os.listdir(input_dir):
        path = input_dir + "/" + filename # 
        print("processing... ", path)
        color_img = cv2.imread(path)#
        gray_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)
        ret, binary_img = cv2.threshold(gray_img, 1, 255,cv2.THRESH_BINARY)
        cv2.imwrite(output_dir+'/'+filename,binary_img )




if __name__ == '__main__':
    input_dir = r"C:\Users\Alex\Desktop\499 project\dataset process\SEGMENTATION"  
    output_dir = r"C:\Users\Alex\Desktop\499 project\dataset process\SEGMENTATION2" 
    convert(input_dir, output_dir)
