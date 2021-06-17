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

import pathlib

import numpy

print(tf.__version__)

data_dir = pathlib.Path(r'D:\DATA-USERS\Ambre Lamouchi\GitHub\stage-ENS-PLATIM-M1\tutoriel Unet\cell_nuclei')
print(type(data_dir))

image_count = len(list(data_dir.glob('*/*.png')))
print(image_count)

img_train = list(data_dir.glob('img_train/*'))
test = tf.keras.preprocessing.image_dataset_from_directory(data_dir, labels='inferred')
print(test.class_names , "  ", type(test))
print()
print()
print()
print(type(test))
print(test.take(1))

class_names = test.class_names

def reschearch():

    
# plt.figure(figsize=(10, 10))
# for images, labels in test.take(1):
#   for i in range(9):
#     ax = plt.subplot(3, 3, i + 1)
#     plt.imshow(images[i].numpy().astype("uint8"))
#     plt.title(class_names[labels[i]])
#     plt.axis("off")
# plt.show()