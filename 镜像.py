# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 00:52:56 2021

@author: Alex
"""
import os
import cv2
import numpy as np
import random
from PIL import Image
import shutil

'''

'''
def convert(input_dir, output_dir):
    for filename in os.listdir(input_dir):
        path = input_dir + "/" + filename # 
        print("processing... ", path)
        gt_img = cv2.imread(path)#
        
        img_mirror = cv2.flip(gt_img, 1)
        
        cv2.imwrite(output_dir+'/'+filename,img_mirror)




if __name__ == '__main__':
    #input_dir = r"C:\Users\Alex\Desktop\414 presentation\data\train1500"  
    #output_dir = r"C:\Users\Alex\Desktop\499 project\dataset\synthetic" 
    input_dir = r"C:\Users\Alex\Desktop\鸭脖图标"
    output_dir = r"C:\Users\Alex\Desktop\鸭脖图标"
    convert(input_dir, output_dir)

