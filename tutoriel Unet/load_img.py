import numpy as np
import os
import PIL
import PIL.Image
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import tensorflow_datasets as tfds

from tensorflow_examples.models.pix2pix import pix2pix

import tensorflow_datasets as tfds

from IPython.display import clear_output
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
print(tf.__version__)

import pathlib
# dataset_url = "https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz"
dataset_url = "D:\DATA-USERS\Ambre Lamouchi\GitHub\stage-ENS-PLATIM-M1\tutoriel Unet\cell_nuclei_train_f_only"

# create a data generator
datagen = tf.keras.preprocessing.image.ImageDataGenerator()

# load and iterate training dataset
train_img = datagen.flow_from_directory('cell_nuclei_train_f_only', class_mode='binary')

train_masque = datagen.flow_from_directory('cell_nuclei_train_label_f_only', class_mode='binary')

# PIL.Image.open("./cell_nuclei_train_f_only/class1/0_t.png").show()



print(os.path.exists("./cell_nuclei_train_f_only/class1/"+"1.png"))
print(os.path.exists("./cell_nuclei_train_f_only/class1/"+"0_t.png"))

plt.figure(figsize=(15, 15))


for i in range(0,2):

    name_img = train_img.filenames[i].split("\\")[1]
    print(name_img)
    plt.subplot(1, 2, i+1)
    plt.title("euhh")
    img = PIL.Image.open("./cell_nuclei_train_f_only/class1/"+name_img)
    
    print(type(img))
    plt.imshow(img)
    plt.axis('off')

plt.show()

# print(train_masque)


# print(len(train_it.classes))