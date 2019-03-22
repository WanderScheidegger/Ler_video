# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 23:46:22 2017

@author: ee4yo
"""

import numpy as np
import cv2
import os                  # Lida com diretorios
from tqdm import tqdm      # barra de porcentagem.

IMG_DIR = 'img/'
VIDEO_DIR = 'videos/'

def criar_fotos(label):
    cap = cv2.VideoCapture(VIDEO_DIR+label)
    frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(frames)
    n = 0
    while(cap.isOpened()) and n<frames:
        
        foto = label.split('.')[-2]
        ret, frame = cap.read()
        cv2.imshow('frame',frame)
        num = str(n)
                    
        nome = IMG_DIR + foto  +  num + '.jpg'
        
        if (n % 10 == 0):
            cv2.imwrite(nome, frame, [cv2.IMWRITE_JPEG_QUALITY, 100])
            img = cv2.imread(nome,cv2.IMREAD_COLOR)
                    
        n=n+1
        
    cap.release()
    cv2.destroyAllWindows()

for video in tqdm(os.listdir(VIDEO_DIR)):
    criar_fotos(video)
