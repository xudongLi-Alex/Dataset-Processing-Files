# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 10:16:53 2021

@author: Alex
"""

import cv2
import numpy as np
from PIL import Image

def get_mask_image(mask, left_top, right_top, left_bottom, right_bottom):

    contours = np.array([[left_top, left_bottom, right_bottom, right_top]], dtype=np.int)
    mask_image = cv2.drawContours(mask, contours, -1, (0, 0, 255), 2)  

    return mask_image

if __name__ == '__main__':
    
    image_path = r"C:\Users\Alex\Desktop\499 project\xudong9-CBDNet-pytorch-master\CBDNet-pytorch\result\output test2\output (1).png" # 加载某张图像

    original_image = cv2.imread(image_path)
    # print(original_image.shape)
    original_image_width = original_image.shape[1]
    original_image_height = original_image.shape[0]

    left_top = [50,50] # 左上角的坐标
    right_top = [100,50] # 右上角的坐标
    left_bottom = [50,100] # 左下角的坐标
    right_bottom = [100,100] # 右下角的坐标

    mask = original_image.copy()
    mask_image = get_mask_image(mask, left_top, right_top, left_bottom, right_bottom)

    x1 = min(left_top[0], right_top[0], left_bottom[0], right_bottom[0])
    x2 = max(left_top[0], right_top[0], left_bottom[0], right_bottom[0])
    y1 = min(left_top[1], right_top[1], left_bottom[1], right_bottom[1])
    y2 = max(left_top[1], right_top[1], left_bottom[1], right_bottom[1])
    hight = y2 - y1
    width = x2 - x1
    crop_img = original_image[y1:y1 + hight, x1:x1 + width] 


    img = Image.fromarray(crop_img)


    img = img.resize((original_image_width, original_image_height))

    left_top = [0, 0] 
    right_top = [original_image_width, 0]  
    left_bottom = [0, original_image_height] 
    right_bottom = [original_image_width, original_image_height] 
    img = np.array(img)
    mask_crop_img = get_mask_image(img, left_top, right_top, left_bottom, right_bottom)

    result_img = np.vstack((mask_image, mask_crop_img))
    cv2.imwrite("./result.jpg", result_img)
