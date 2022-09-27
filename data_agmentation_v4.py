# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 11:58:57 2022

@author: Usuario
"""
import albumentations as A
import os
import cv2
import sys
from numpy import genfromtxt
import numpy as np

import time



def getTransform(loop): 
    if loop == 0: 
        transform = A.Compose([ A.HorizontalFlip(p=1),
        ], bbox_params = A.BboxParams(format='yolo', min_visibility = 0.1)) 
    elif loop == 1: 
        transform = A.Compose([ A.augmentations.transforms.ColorJitter(saturation = 0.3, p=1),
        ], bbox_params = A.BboxParams(format='yolo', min_visibility = 0.1))
    elif loop == 2: 
        transform = A.Compose([ A.augmentations.transforms.ColorJitter(contrast = 0.2, p=1),
        ], bbox_params = A.BboxParams(format='yolo', min_visibility = 0.1))
    elif loop == 3: 
        transform = A.Compose([ A.augmentations.Rotate(limit = 98, interpolation = 1, border_mode=cv2.BORDER_CONSTANT, value = None, mask_value = None, always_apply = False, p=1),
        ], bbox_params = A.BboxParams(format='yolo', min_visibility = 0.1)) 
    elif loop == 4:
        transform = A.Compose([ A.augmentations.RandomScale(scale_limit = 0.2, interpolation=1, always_apply=False, p=1),
        ], bbox_params = A.BboxParams(format='yolo', min_visibility = 0.1)) 
    elif loop == 5: 
        transform = A.Compose([ A.VerticalFlip(p=1),
        ], bbox_params = A.BboxParams(format='yolo', min_visibility = 0.1)) 
    elif loop == 6:
        transform = A.Compose([
            A.RandomScale(scale_limit = 0.2, interpolation=1, always_apply=False, p=1),
            A.augmentations.Rotate(limit = 98, interpolation = 1, border_mode=cv2.BORDER_CONSTANT, value = None, mask_value = None, always_apply = False, p=1),
        ], bbox_params=A.BboxParams(format='yolo', min_visibility = 0.1))
    elif loop == 7:
        transform = A.Compose([
            A.augmentations.transforms.GlassBlur(sigma=0.7, max_delta=4, iterations=2, always_apply=False, mode='fast', p=0.5),
            A.augmentations.transforms.GaussianBlur(blur_limit=(3, 7), sigma_limit=0, always_apply=False, p=0.5),
        ], bbox_params=A.BboxParams(format='yolo', min_visibility = 0.1))

    return transform 

def readFilesinFolder(path):
    lista=[]
    
    for filename in os.listdir(path): 
        
        if filename.endswith('.jpg') or filename.endswith('.png'): 
            title, ext = os.path.splitext(os.path.basename(filename)) 
            lista.append(title+ext)
            
    return lista 

def start(): 
    
    labels = ['car','person','smoke','debris','flood','emergency-vehicle','fire']
    
    files = readFilesinFolder(originFolder)
    
    for k in range(8): 
        transform = getTransform(k) 
        
        for j in files: 
            try: 
                image = cv2.imread(j) #image = cv2.imread(j+'.jpg')
                #image = np.array(image)
                tmp = j[:-4]
                bboxes = genfromtxt(originPath+tmp+'.txt',dtype = str, delimiter=' ')

                #bboxes = bboxes.tolist()
                
                tmp3 = [0.0, 0.0, 0.0, 0.0, 0.0]
                tmp2 = []
                for bbox in bboxes:
                    '''
                    for x in len(bbox):
                        tmp3.append(float(bbox[x]))
                    bboxes.append(tmp3)
                    tmp3.clear()
                    '''
                    #for i in range(bbox):
                        #ESTA CONVERSION NO SE ESTA HACIENDO!!!!!! 
                    tmp3[0] = float(bbox[0])
                    tmp3[1] = float(bbox[1])
                    tmp3[2] = float(bbox[2])
                    tmp3[3] = float(bbox[3])
                    tmp3[4] = float(bbox[4])
                    tmp2.append(tmp3)
                    tmp3 = [0.0, 0.0, 0.0, 0.0, 0.0]
                
                for bbox in tmp2:
                    if(bbox[0]==0.0):
                        bbox.append(labels[0])
                        bbox.pop(0)
                    elif(bbox[0]==1.0):
                        bbox.append(labels[1])
                        bbox.pop(0)
                    elif(bbox[0]==2.0):
                        bbox.append(labels[2])
                        bbox.pop(0)
                    elif(bbox[0]==3.0):
                        bbox.append(labels[3])
                        bbox.pop(0)
                    elif(bbox[0]==4.0):
                        bbox.append(labels[4])
                        bbox.pop(0)
                    elif(bbox[0]==5.0):
                        bbox.append(labels[5])
                        bbox.pop(0)
                    elif(bbox[0]==6.0):
                        bbox.append(labels[6])
                        bbox.pop(0)

                transformed = transform(image=image, bboxes=tmp2)
                transformed_image = transformed['image']
                transformed_bboxes = transformed['bboxes']
                with open(destPath+"train/labels/"+str(k)+"_"+tmp.replace("frame","") + ".txt", 'w') as f:
                    for x in transformed_bboxes:
                        if (x[-1]=="car"):
                            f.write("0 %s %s %s %s\n" % (round(x[0],6), round(x[1],6), round(x[2],6), round(x[3],6))) 
                        elif (x[-1]=="person"):
                            f.write("1 %s %s %s %s\n" % (round(x[0],6), round(x[1],6), round(x[2],6), round(x[3],6)))
                        elif (x[-1]=="smoke"):
                            f.write("2 %s %s %s %s\n" % (round(x[0],6), round(x[1],6), round(x[2],6), round(x[3],6)))
                        elif (x[-1]=="debris"):
                            f.write("3 %s %s %s %s\n" % (round(x[0],6), round(x[1],6), round(x[2],6), round(x[3],6)))
                        elif (x[-1]=="flood"):
                            f.write("4 %s %s %s %s\n" % (round(x[0],6), round(x[1],6), round(x[2],6), round(x[3],6)))
                        elif (x[-1]=="emergency-vehicle"):
                            f.write("5 %s %s %s %s\n" % (round(x[0],6), round(x[1],6), round(x[2],6), round(x[3],6)))
                        elif (x[-1]=="fire"):
                            f.write("6 %s %s %s %s\n" % (round(x[0],6), round(x[1],6), round(x[2],6), round(x[3],6)))
           
                cv2.imwrite(destPath+"train/images/"+str(k)+"_"+tmp+j[-4:], transformed_image) 
            except: 
                print("FAILED TO READ IMAGE: "+j)
                print(sys.exc_info()) 

originPath = "C:/Users/Usuario/Desktop/Facultad/Cuarto GIERM/Trabajo Fin de Grado/Etiquetado/train_data/train/labels/"  
destPath = "C:/Users/Usuario/Desktop/Facultad/Cuarto GIERM/Trabajo Fin de Grado/Etiquetado/train_data_augmented/" 
originFolder= "C:/Users/Usuario/Desktop/Facultad/Cuarto GIERM/Trabajo Fin de Grado/Etiquetado/train_data/train/images/" 
files=[]
if __name__ == "__main__": 
    start() 