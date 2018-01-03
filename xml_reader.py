# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 12:19:42 2018

@author: mbgnwlr2
"""

import os
import numpy as np
from PIL import Image
import xml.etree.ElementTree as ET
import glob

os.chdir('C:\\Users\\mbgnwlr2\\Documents\\PhD_LabStuff\\Rad_Stitch_Practice')

##Analysis of .xml files
print('image', 'x axis position (mm)', 'y axis position (mm)', 'magnification (mm)', 'rotation (degrees)', 'tilt (degrees)', 'imaging (mm)') 

#Produces a list of files starting with "AlSiC..." and ending in ".xml"
filenames = sorted(glob.glob('AlSiC_monosheet_*.xml'))
filenames = filenames[0:10]

np.xpos = [] #list to add x coordinates
np.ypos = [] #list to add y coordiantes

i = 0 #iteration counter

#reading each .xml file in turn and extracting the data
for f in filenames:

    tree = ET.parse(f)

    root = tree.getroot()

    x1 = float(root[5][0].text)
    y1 = float(root[5][1].text)
    mag = float(root[5][2].text)
    rot = float(root[5][3].text)
    tilt = float(root[5][4].text)
    img = float(root[5][5].text)

    np.xpos.insert(i, x1+129.504)
    np.ypos.insert(i, y1-301.876)
    
    i = i+1

    #print all values in list below headers defined above
    print ('%-6i%-21f%-21f%-19i%-19i%-15i%-13i' % (i, x1, y1, mag, rot, tilt, img))
    
#convert from mm to pixels (value measured in imageJ)
px = 117.533 #(pixels/mm)

#end with lists of x and y coordinates in units of pixels
x = np.multiply(np.xpos, px)
y = np.multiply(np.ypos, px) 


##Combination of .tif files

#begin with a blank background to stitch each image to
background = Image.new('I;16', (40000, 4000))

#Produces a list of files starting with "AlSiC..." and ending in ".tif"
images = sorted(glob.glob('AlSiC_monosheet_*.tif'))
images = images[0:10]

ix = 9 #iteration counter for x axis

for f in images:
    im = Image.open(f)

    background.paste(im, (int(round(x[ix])), 0)) #lines image up with ix-th coordinate of list x
    
    ix = ix-1

background.save('stitching_attempt_1.tif') #saves final image as "stitching_attempt_1