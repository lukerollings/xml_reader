# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 12:19:42 2018

@author: mbgnwlr2
"""

import os
import xml.etree.ElementTree as ET

os.chdir('C:\\Users\\mbgnwlr2\\Documents\\PhD_LabStuff\\Radiography_17_12_20')


tree = ET.parse('AlSiC_monosheet_1_LHS.tif.profile.xml')

root = tree.getroot()

#print('x axis position (mm):')  
#print(root[5][0].text)
#
#print('y axis position (mm)')
#print(root[5][1].text)
#
#print('magnification (mm)')
#print(root[5][2].text)
#
#print('rotation (degrees)')
#print(root[5][3].text)
#
#print('tilt (degrees)')
#print(root[5][4].text)
#
#print('imaging (mm)')
#print(root[5][5].text)


x1 = float(root[5][0].text)
y1 = float(root[5][1].text)
mag = float(root[5][2].text)
rot = float(root[5][3].text)
tilt = float(root[5][4].text)
img = float(root[5][5].text)

print('x axis position (mm)', 'y axis position (mm)', 'magnification (mm)', 'rotation (degrees)', 'tilt (degrees)', 'imaging (mm)') 

print ('%-21i%-21i%-19i%-19i%-15i%-13i' % (x1, y1, mag, rot, tilt, img))