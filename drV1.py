# -*- coding: utf-8 -*-
"""
Created on Fri May 22 15:37:00 2015

@author: Aditya
"""

import numpy as np
import os
from scipy import ndimage
import scipy.sparse

#import kmeans
from matplotlib import pyplot as plt
import pandas as pd

import cv2


# Set the location of the training directory
train_dir = '/media/Seagate Expansion Drive/DiabeticRetinopathy/train/train/'
# List all of the files in the training set
img_list = os.listdir(train_dir)


# Filter files names of all left images
left_img = filter(lambda x: x[-9:-5] =='left' ,img_list)
# filter for right images
right_img = filter(lambda x: x[-10:-5] =='right' ,img_list)

# Plot a sample left image (original image, resized(256,256), grey scale image)
img = cv2.imread(train_dir + left_img[56])

img1 = cv2.resize(img,(256,256))

cimg = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

fig,imgplt = plt.subplots(1,3)

imgplt[0].imshow(img)

imgplt[1].imshow(img1)

imgplt[2].imshow(cimg,cmap='gray')

plt.show()






