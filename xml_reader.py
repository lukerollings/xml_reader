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
import matplotlib.pyplot as plt

os.chdir('C:\\Users\\mbgnwlr2\\Documents\\PhD_LabStuff\\Radiography_17_12_20')

##Analysis of .xml files
print('image', 'x axis position (mm)', 'y axis position (mm)', 'magnification (mm)', 'rotation (degrees)', 'tilt (degrees)', 'imaging (mm)') 

#Produces a list of files starting with "AlSiC..." and ending in ".xml"
filenames = sorted(glob.glob('AlSiC_monosheet_*.xml'))
filenames = filenames[0:100]

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

x = np.multiply(np.xpos, px)
y = np.multiply(np.ypos, px) 

plt.scatter(x, y)


##Combination of .tif files

#begin with a blank background to stitch each image to
background = Image.new('I;16', (36500, 36500))

width, height = background.size

x = (width-4000) - x  #ensures images are mapped in correct order
#the scan was captured (hence the image was saved) in the opposite order to that which PIL assigns coordinates

#Produces a list of files starting with "AlSiC..." and ending in ".tif"
images = sorted(glob.glob('AlSiC_monosheet_*.tif'))
images = images[0:100]

ix = 0 #iteration counter for x axis
iy = 0

#reads each .tif file in turn and assigns it to the appropriate coordinates on background image
for f in images:
    im = Image.open(f)

    background.paste(im, (int(round(x[ix])), int(round(y[iy])))) #lines image up with ix-th coordinate of list x
    
    ix = ix+1
    iy = iy+1

background.save('stitching_attempt_1.tif') #saves final image as "stitching_attempt_1.tif"