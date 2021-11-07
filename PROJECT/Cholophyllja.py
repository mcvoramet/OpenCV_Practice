# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 21:36:14 2021

@author: Satha Srisura
"""

import cv2
import numpy as np

def Cholophyll(img):

    blue, green, red = cv2.split(img) # Split the image into its channels
    R = img[:,:,0]
    G = img[:,:,1]
    B = img[:,:,2]

    np.mean(R)
    np.mean(G)
    np.mean(B)

    print(np.mean(R))
    print(np.mean(G))
    print(np.mean(B))

    r = np.mean(R)/[np.mean(R)+np.mean(G)+np.mean(B)]
    g = np.mean(G)/[np.mean(R)+np.mean(G)+np.mean(B)]
    b = np.mean(B)/[np.mean(R)+np.mean(G)+np.mean(B)]

    Chlorophyll = (-88*r)+(62*g)+(192*b);
    
    return Chlorophyll
