# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 19:18:40 2021

@author: Alex
"""
import matplotlib.pyplot as plt
import numpy as np
import numpy.random as randn
import pandas as pd
from pandas import Series,DataFrame
from pylab import mpl
import skimage.metrics as metrics
import os
import cv2
import numpy as np
import random
import skimage
import skimage.metrics as metrics
from scipy.optimize import curve_fit
import scipy.io as sio
import scipy.misc

def visualization(data):
    fig, ax = plt.subplots(1)
    ax.plot(data)

    # 设置刻度范围
    if data==PSNR_LIST:
        ax.set_xlim([0, 1])
    else:
        ax.set_xlim([0, 1])
    # 设置显示的刻度(记号)
    ax.set_xticks(range(0,5,1))
    
    # 设置刻度标签
    #ax.set_xticklabels(['one', 'two', 'three', 'four', 'five'],
    #                            rotation=30, fontsize='small')
    
    # 设置坐标轴标签
    ax.set_xlabel('X:...')
    ax.set_ylabel('Y:...')
    
    # 设置标题
    if data==PSNR_LIST:
        ax.set_title('OUR PSNR')
    else:
        ax.set_title('OUR SSIM')



input_dir1 = r"C:\Users\Alex\Desktop\499 project\结果\原图"  
input_dir2 = r"C:\Users\Alex\Desktop\499 project\结果\融合图\demo_final" 
result_dir= r"C:\Users\Alex\Desktop\499 project\compare/"
def averagenum(num):
    nsum = 0
    for i in range(len(num)):
        nsum += num[i]
    return nsum / len(num)

PSNR_LIST=[]
SSIM_LIST=[]

i=0
for i in range(1,4):
    img1=input_dir1+"/"+str(i)+".png"
    #print(img1)
    test_img = cv2.imread(img1)
    #print(test_img.shape)
    test_img = test_img[:,:,::-1] / 255.0
    test_img = np.array(test_img).astype('float32')
    #print(test_img)
    
    img2=input_dir2+"/"+str(i)+".png"
    out_img = cv2.imread(img2)
    out_img = cv2.resize(out_img,(180,180))
    #print(out_img.shape)
    out_img = out_img[:,:,::-1] / 255.0
    out_img = np.array(out_img).astype('float32')
    
    #temp = np.concatenate((test_img, out_img), axis=1)
    #scipy.misc.toimage(temp*255, high=255, low=0, cmin=0, cmax=255).save(result_dir + 'test_%d.jpg'%(i))
    i+=1
    '''
    PSNR calculate
    '''
    PSNR = skimage.metrics.peak_signal_noise_ratio(test_img, out_img)
    PSNR_LIST.append(PSNR)
    print(PSNR)
        
    '''
    SSIM calculate
    '''
    SSIM=skimage.metrics.structural_similarity(test_img, out_img, multichannel=True)
    SSIM_LIST.append(SSIM)
    print(SSIM)
    
    
print("Average PSNR for test set: ",averagenum(PSNR_LIST))
print("Average SSIM for test set: ",averagenum(SSIM_LIST))



visualization(PSNR_LIST)
visualization(SSIM_LIST)
