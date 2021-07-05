# 
import os
from PIL import Image
import cv2
import numpy as np


H = 256
W = 256


test_masks = os.listdir("data/test_masks/")
train_masks = os.listdir("data/train_masks/train/")
val_masks = os.listdir("data/val_masks/val/")

tab = [0]*256
imgs = []
for img in test_masks:
    x = cv2.imread("data/test_masks/"+img, cv2.IMREAD_GRAYSCALE)
    x = cv2.resize(x, (W, H))
    for h in range (0, 256):
        for l in range (0, 256):
            if(x[h][l] == 255):
                x[h][l] = 2
            else: 
                if(x[h][l] == 0):
                    x[h][l] = 0
                else:
                    x[h][l] = 1
    imgs.append(x)
    cv2.imwrite("data_2/test_masks/"+img,x)

for img in train_masks:
    x = cv2.imread("data/train_masks/train/"+img, cv2.IMREAD_GRAYSCALE)
    x = cv2.resize(x, (W, H))
    for h in range (0, 256):
        for l in range (0, 256):
            if(x[h][l] == 255):
                x[h][l] = 2
            else: 
                if(x[h][l] == 0):
                    x[h][l] = 0
                else:
                    x[h][l] = 1

    imgs.append(x)
    cv2.imwrite("data_2/train_masks/train/"+img,x)

for img in val_masks:
    x = cv2.imread("data/val_masks/val/"+img, cv2.IMREAD_GRAYSCALE)
    x = cv2.resize(x, (W, H))

    # print( x[255][255] )

    for h in range (0, 256):
        for l in range (0, 256):
            if(x[h][l] == 255):
                x[h][l] = 2
            else: 
                if(x[h][l] == 0):
                    x[h][l] = 0
                else:
                    x[h][l] = 1
    imgs.append(x)
    cv2.imwrite("data_2/val_masks/val/"+img,x)

image_y = Image.fromarray(imgs[0].astype(np.uint8))
# image_y.show()
# for i in tab:
#     print(i)
# print(test_masks[0])