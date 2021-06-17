import os
from os import listdir
from os.path import isfile, join
import re

# importing shutil module 
import shutil 

fichiersf1 = [f for f in listdir("./unet_img/img") if isfile(join("./unet_img/img", f))]
fichiersf2 = [f for f in listdir("./unet_img/label") if isfile(join("./unet_img/label", f))]

print(len(fichiersf1))
print(len(fichiersf2))

size = len(fichiersf1)

print(fichiersf1[200])
print(fichiersf2[200])

os.mkdir("./unet_img/img_train/")
os.mkdir("./unet_img/label_train/")

os.mkdir("./unet_img/img_test/")
os.mkdir("./unet_img/label_test/")


for i in range (0, int(size/2)):
    original_img_train = "./unet_img/img/"+ fichiersf1[i]
    dest_img_train = "./unet_img/img_train/"+ fichiersf1[i]

    original_label_train = "./unet_img/label/"+ fichiersf2[i]
    dest_label_train = "./unet_img/label_train/"+ fichiersf2[i]
    print(original_label_train, "  ", dest_label_train)
    shutil.move(original_img_train, dest_img_train)
    shutil.move(original_label_train, dest_label_train)


for i in range(int(size/2)+1, size):
    original_img_test = "./unet_img/img/"+ fichiersf1[i]
    dest_img_test = "./unet_img/img_test/"+ fichiersf1[i]

    original_label_test = "./unet_img/label/"+ fichiersf2[i]
    dest_label_test = "./unet_img/label_test/"+ fichiersf2[i]

    shutil.move(original_img_test, dest_img_test)
    shutil.move(original_label_test, dest_label_test)