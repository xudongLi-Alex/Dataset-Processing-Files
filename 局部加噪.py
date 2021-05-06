# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 11:30:17 2021

@author: Alex
"""
import os
import cv2
import numpy as np
import random
import matplotlib.pyplot as plt
input_dir1 = r"C:\Users\Alex\Desktop\499 project\特征融合\feature_imgs-20210420T055940Z-001\feature_imgs/1.png"
input_dir2 = r"C:\Users\Alex\Desktop\499 project\特征融合\test30_cbd-20210420T084216Z-001\test30_cbd/1.png" 
input_dir3=r"C:\Users\Alex\Pictures\IQIYISnapShot\1.jpg"
def gaussian_noise(img, feature_img, sigma):

    temp_image = np.float64(np.copy(img))
    feature_img = np.float64(np.copy(feature_img))
    h, w, _ = feature_img.shape
    noise = np.random.randn(h, w) * sigma
    gaussian_image = np.zeros(temp_image.shape, np.float64)
    
    for i in range(len(feature_img)):
        for j in range(len(feature_img[0])):
            if feature_img[i][j][0] ==0 and feature_img[i][j][1] ==0 and feature_img[i][j][2] ==0:
                gaussian_image[i][j][0]=temp_image[i][j][0]+ noise[i][j]
                gaussian_image[i][j][1]=temp_image[i][j][1]+ noise[i][j]
                gaussian_image[i][j][2]=temp_image[i][j][2]+ noise[i][j]
            else:
                gaussian_image[i][j][0]=temp_image[i][j][0]
                gaussian_image[i][j][1]=temp_image[i][j][1]
                gaussian_image[i][j][2]=temp_image[i][j][2]
                
    return gaussian_image





feature_img = cv2.imread(input_dir1)
org_img = cv2.imread(input_dir2)

img=gaussian_noise(org_img,feature_img,5)

plt.imshow(img)

plt.show()
