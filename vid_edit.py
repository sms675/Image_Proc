# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 13:25:07 2017

@author: stephen
"""
import sys
sys.path.insert(0,'/home/stephen/Code/Python/venv/local/lib/python2.7/site-packages')
import pylab
import os
import imageio
import matplotlib.pyplot as plt
from scipy import misc
from scipy import ndimage
import numpy as np
import PIL
from PIL import Image

im_red = Image.new("RGB", (1280,720), "red")
im_blue = Image.new("RGB", (1280,720), "blue")
im_green = Image.new("RGB", (1280,720), "green")
im_yellow = Image.new("RGB", (1280,720), "yellow")
im_orange = Image.new("RGB", (1280,720), "orange")
im_purple = Image.new("RGB", (1280,720), "purple")
im_white = Image.new("RGB", (1280,720), "white")
current_path = os.path.dirname(os.path.realpath('__file__'))

filename = current_path + '/ppo_2.mp4'; print filename
vid = imageio.get_reader(filename, 'ffmpeg')
fps = vid.get_meta_data()['fps']

blur_only = False
out_file = current_path + '/video.mp4'
writer = imageio.get_writer('video.mp4', fps=fps)
count = 0

for num in range(0,len(vid)):
    print 'processing frame %s...' %(num) 
    image = vid.get_data(num)

    if (num > 2200 and num < 2300):
        if blur_only == False:        
            im = ndimage.gaussian_filter(image, 8)
            image_x = ndimage.sobel(im, axis=0, mode='constant')
            image_y = ndimage.sobel(im, axis=1, mode='constant')
            image = np.hypot(image_x,image_y)
            image = np.uint8(image)
        else:    
            im = ndimage.gaussian_filter(image, 12)
            image = im
           
    if num >= 2200 and num <=2700:
        x = 10 #factor for color frequency (high is lower)
    elif num >= 7000 and num <= 7600:
        x = 1
         
    if (num >= 2200 and num <= 2700) or (num >= 7000 and num <= 7600):
        count += 1
        im1 = PIL.Image.fromarray(image)
        if count <= (5*x):
            color_frame = im_red
        elif count > (5*x) and count <= (10*x):
            color_frame = im_blue
        elif count > (10*x) and count <= (15*x):
            color_frame = im_green
        elif count > (15*x) and count <= (20*x):
            color_frame = im_yellow
        elif count > (20*x) and count <= (25*x):
            color_frame = im_orange
        elif count > (25*x) and count <= (30*x):
            color_frame = im_purple
        elif count > (30*x) and count <= (35*x):
            color_frame = im_white
        elif count > (35*x):    
            count = 0
        image = np.array(PIL.Image.blend(im1,color_frame,.4))
     
    writer.append_data(image)
writer.close()



'''
count = 0
#7000-7600, multiples of 5

for num in range(2200,2700):
    #print 'processing frame %s...' % (num)
    #image = vid.get_data(num)
    im1 = PIL.Image.fromarray(image)
    count += 1
    if count <= 50:
        color_frame = im_red
    elif count > 50 and count <= 100:
        color_frame = im_blue
    elif count > 100 and count <= 150:
        color_frame = im_green
    elif count > 150 and count <= 200:
        color_frame = im_yellow
    elif count > 200 and count <= 250:
        color_frame = im_orange
    elif count > 250 and count <= 300:
        color_frame = im_purple
    elif count > 300 and count <= 350:
        color_frame = im_white
    elif count > 350:    
        count = 0
    newim = np.array(PIL.Image.blend(im1,color_frame,.4))
    writer.append_data(newim)
    
    
    
writer.close()
    

# if (num > 1400 and num < 1530) or (num > 1860 and num < 1920) or\
#       (num > 3800 and num < 3880) or (num > 5900 and num < 6100) or\
#       (num > 6700 and num < 6720) or (num > 6900 and num < 6920) or\
#       (num > 7000 and num < 7020) or (num > 7050 and num < 7070) or\
#       (num > 7300 and num < 7315) or (num > 7400 and num < 7420) or\
#       (num > 7500 and num < 7515) or (num > 7600 and num < 7615) or\
#       (num > 7700 and num < 7720) or (num > 7850 and num < 7870):
'''