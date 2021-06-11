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

# print(fichiersf1[0:3])
# print(fichiersf2[0:3])

fichiersf1_0 = []
fichiersf2_0 = []

images = []
labels = []

for i in range(0,len(fichiersf1)):
    # print(fichiersf1[i]," - ",fichiersf1[i].split('_'))
    fichiersf1_0.append(fichiersf1[i].split('_')[0])
    # print(fichiersf1[i])

for i in range(0,len(fichiersf2)):
    fichiersf2_0.append(fichiersf2[i].split('_')[0])

# print(fichiersf1[0:3])

for i in fichiersf1:
    if not(i.split('_')[0] in fichiersf2_0):
        # print(i)
        # if(i.i.split('_')[1])
        # print(i.split(".")[0])
        # print(re.findall( '[a-zA-Z]', i.split(".")[0]))


        # print(re.findall( '[a-zA-Z]', i.split(".")[0]))
        # print(to_str(re.findall( '[a-zA-Z]', i.split(".")[0])))

        

        # print(re.findall( '[0-9]', i.split(".")[0]))
        est_tf = not(re.findall( 'tf', i.split(".")[0]) is None)
        est_tr = not(re.findall( 'tr', i.split(".")[0]) is None)
        # print(est_tf)
        # print(est_tr)

        # print(re.findall( '[a-zA-Z]', i.split(".")[0]))
        
        # print(to_str(re.findall( '[0-9]', i.split(".")[0]))+"l.png")

        # os.remove("./class1/" + i + "_t.png")
        if(to_str(re.findall( '[a-zA-Z]', i.split(".")[0])) == "t"):
            if(not (to_str(re.findall( '[0-9]', i.split(".")[0]))+"l.png" in fichiersf2) ):
                print("non t")
                nbsup1 = nbsup1 + 1

                print(i)

        if(to_str(re.findall( '[a-zA-Z]', i.split(".")[0])) == "tf"):
            if(not (to_str(re.findall( '[0-9]', i.split(".")[0]))+"lf.png" in fichiersf2) ):
                nbsup1 = nbsup1 + 1
                print("non tf")

        if(to_str(re.findall( '[a-zA-Z]', i.split(".")[0])) == "tr"):
            if(not (to_str(re.findall( '[0-9]', i.split(".")[0]))+"lr.png" in fichiersf2) ):
                print(to_str(re.findall( '[0-9]', i.split(".")[0]))+"lr.png")
                nbsup1 = nbsup1 + 1

                print("non tr")
    print(to_str(i.split('_')[1]))
        
        
print(nbsup1)

# for i in fichiersf2:
#     if not(i in fichiersf1):
#         # os.remove("./masque/" + i + "_l.png")
#         nbsup2 = nbsup2 + 1
# print(nbsup2)

# print(fichiersf2)
