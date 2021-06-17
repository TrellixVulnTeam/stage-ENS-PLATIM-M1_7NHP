import os
from os import listdir
from os.path import isfile, join
import re

fichiersf1 = [f for f in listdir("./unet_img/img") if isfile(join("./unet_img/img", f))]
fichiersf2 = [f for f in listdir("./unet_img/label") if isfile(join("./unet_img/label", f))]
for elm in fichiersf1[:5]:
   print(elm.split('.')[0])
print(" ")
print((fichiersf1[0].split('_')[0] + "_lf.png") in fichiersf2) 
print(fichiersf1[:5])