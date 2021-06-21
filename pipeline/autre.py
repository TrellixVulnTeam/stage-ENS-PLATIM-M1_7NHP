import os
from os import listdir
from os.path import isfile, join
import re

def to_str(list):
    str = ""
    for i in list:
        str += i
    return str

fichiersf1 = [f for f in listdir("class1") if isfile(join("class1", f))]
fichiersf2 = [f for f in listdir("masque") if isfile(join("masque", f))]

nbsup1 = 0
nbsup2 = 0

print(fichiersf1[0])
print(fichiersf2[0])

# renommer les fichier


fichier = open("data.csv", "a")
taille = len(fichiersf1)
for i in range(0, int(taille*0.70)):
    os.rename('.\class1\\'+fichiersf1[i],'.\data\\train_img\\img'+str(i)+".png")
    print("img",i, " ", "masque",i)
    os.rename('.\masque\\'+fichiersf2[i],'.\data\\train_mask\\mask'+str(i)+".png")

for i in range(int(taille*0.70)+1, int(taille*0.70) + int(taille*0.20)):
    os.rename('.\class1\\'+fichiersf1[i],'.\data\\val_img\\img'+str(i)+".png")
    print("img",i, " ", "masque",i)
    os.rename('.\masque\\'+fichiersf2[i],'.\data\\val_mask\\mask'+str(i)+".png")

for i in range(int(taille*0.70) + int(taille*0.20)+1, taille):
    os.rename('.\class1\\'+fichiersf1[i],'.\data\\test_img\\img'+str(i)+".png")
    print("img",i, " ", "masque",i)
    os.rename('.\masque\\'+fichiersf2[i],'.\data\\test_mask\\mask'+str(i)+".png")

    # os.rename('.\masque\\'+fichiersf2[i],'.\label\\mask'+str(i)+".png")
    # fichier.write(fichiersf1[i]+","+fichiersf2[i]+'\n')

fichier.close()