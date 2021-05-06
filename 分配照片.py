# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 00:52:56 2021

@author: Alex
"""

import os,shutil

for i in range(1,401):
    shutil.copy(r"C:\Users\Alex\Desktop\499 project\train 400\gt ("+str(i)+").png",r'C:\Users\Alex\Desktop\499 project\improve cbd data\gt'+'/Batch '+str(i))
    #shutil.copy(r"C:\Users\Alex\Desktop\499 project\train 400 5\Noisy 5 ("+str(i)+").png",r'C:\Users\Alex\Desktop\499 project\real'+'/Batch '+str(i))
    #shutil.copy(r"C:\Users\Alex\Desktop\499 project\train 400 7\Noisy 7 ("+str(i)+").png",r'C:\Users\Alex\Desktop\499 project\real'+'/Batch '+str(i))
    
