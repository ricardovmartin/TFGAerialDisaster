# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 18:20:26 2022

@author: Usuario
"""

import os

folder = 'C:/Users/Usuario/Desktop/Facultad/Cuarto GIERM/Trabajo Fin de Grado/Etiquetado/train_data/train/labels/'
count = 1
# count increase by 1 in each iteration
# iterate all files from a directory
for file_name in os.listdir(folder):
    # Construct old file name
    source = folder + file_name

    # Adding the count to the new file name and extension
    destination = folder + "datasetDRON_" + str(count) + ".txt"

    # Renaming the file
    os.rename(source, destination)
    count += 1
print('All Files Renamed')

print('New Names are')
# verify the result
res = os.listdir(folder)
print(res)