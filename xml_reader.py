# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 12:19:42 2018

@author: mbgnwlr2
"""

import os
import xml.etree.ElementTree as ET
import glob

os.chdir('C:\\Users\\mbgnwlr2\\Documents\\PhD_LabStuff\\Radiography_17_12_20')

print('x axis position (mm)', 'y axis position (mm)', 'magnification (mm)', 'rotation (degrees)', 'tilt (degrees)', 'imaging (mm)') 

filenames = sorted(glob.glob('AlSiC_monosheet_*.xml'))
filenames = filenames[0:100]

for f in filenames:

    tree = ET.parse(f)

    root = tree.getroot()

    x1 = float(root[5][0].text)
    y1 = float(root[5][1].text)
    mag = float(root[5][2].text)
    rot = float(root[5][3].text)
    tilt = float(root[5][4].text)
    img = float(root[5][5].text)



    print ('%-21i%-21i%-19i%-19i%-15i%-13i' % (x1, y1, mag, rot, tilt, img))