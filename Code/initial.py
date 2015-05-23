# -*- coding: utf-8 -*-
"""
Created on Thu May 21 01:12:20 2015

@author: aditya
"""

import cv2
from skimage import filters
from scipy import ndimage
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('sample/10_left.jpeg')
#img = cv2.resize(img,(256,256))
#img = img[:1000,2000:,:]
#img = cv2.imread('opencv_logo.png',0)
img = cv2.medianBlur(img,5)

cimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cimg = cimg[:1000,2000:,:]
#plt.imshow(cimg,cmap = 'gray')
#plt.imshow(cv2.resize(cv2.Canny(cimg,10,500),(0,0),fx=0.5, fy=0.5),cmap='gray')
filtimg = cv2.resize(cv2.Canny(cimg,10,500),(0,0),fx=0.5, fy=0.5)

circles = cv2.HoughCircles(filtimg,cv2.HOUGH_GRADIENT,1,60,
                            param1=200,param2=10,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

#cv2.imshow('detected circles',cimg)
plt.imshow(cimg,cmap='gray')
cv2.waitKey(0)
cv2.destroyAllWindows()






