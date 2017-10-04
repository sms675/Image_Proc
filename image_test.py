# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 05:42:01 2017

@author: stephen

"""
import os
from scipy import misc
import matplotlib.pyplot as plt
import numpy as np
current_path = os.path.dirname(os.path.realpath('__file__'))


cell_pic = misc.imread('labeled1.png')
#slice out green color channel...
green_chan = cell_pic[:,:,1]



thesho = np.where(green_chan > 110, 1, 0)

misc.imsave('thresh_120.jpg',thresho)
        
#show_image = raw_input('show image? y/n?: ')
#if show_image == 'y':)
plt.imshow(green_chan); plt.show()
# Remove axes and ticks
#plt.axis('off')
# Draw contour lines
#plt.contour(camus, [50, 200])  
plt.hist(green_chan.ravel(), bins=256, range=(80,130))
        
        
        