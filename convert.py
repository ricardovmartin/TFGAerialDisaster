# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 20:24:59 2022

@author: Usuario
"""

from PIL import Image
from os import listdir
import os
from os.path import splitext

target_directory = '.'
target = '.png'
delete = '.jpg'

for file in listdir(target_directory):
    filename, extension = splitext(file)
    
    try:
        if extension not in ['.py', target]:
            im = Image.open(filename + extension)
            im.save(filename + target)
            
            rmvFile = filename + delete
            os.remove(rmvFile)
    except OSError:
        print('Cannot convert %s' % file)        