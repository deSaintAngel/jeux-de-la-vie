# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 02:51:19 2020

@author: julien
"""
### Jeux de la vie ###

#%% Modules
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


#%%
# dimentions 
n = 100
m = 100

img = np.zeros((n,m),dtype=int)
fig  = np.zeros((9,36),dtype=int)
# filtre de convolution pour la sommations
F = np.array([[1, 1, 1],[1, 0, 1],[1, 1, 1]]) 

# Etat initial 
#img[[50, 50, 50], [49, 50, 51]]=1 # Barre 3 points
fig[[4,5,4,5,4,5,6,3,7,2,8,2,8,5,3,7,4,5,6,5,2,3,4,2,3,4,1,5,0,1,5,6,2,3,2,3],[0,0,1,1,10,10,10,11,11,12,12,13,13,14,15,15,16,16,16,17,20,20,20,21,21,21,22,22,24,24,24,24,34,34,35,35]] = 1 # Canon 36 points 
img[45:45+9,32:32+36] = fig
plt.imshow(img)

#%%

## EVOLUTION ##
for i in range(100):  # endless loop
    # tableau ses sommes des voisins
    VoisinSum = signal.convolve(img, F,'same')
    
    # evolution : mort naissance et survie
    naissance = np.where(VoisinSum == 3)
    mort = np.where(VoisinSum <=1) 
    mort2 = np.where(VoisinSum >3)
    
    img[naissance] = 1
    img[mort] = 0
    img[mort2] = 0
    
    plt.imshow(img)
    plt.pause(0.01)
    
    
#[[4,5,4,5,4,5,6,3,7,2,8,2,8,5,3,7,4,5,6,5,2,3,4,2,3,4,1,5,0,1,5,6,2,3,2,3],[0,0,1,1,10,10,10,11,11,12,12,13,13,14,15,15,16,16,16,17,20,20,20,21,21,21,22,22,24,24,24,24,34,34,35,35]]# Canon 36 points 
