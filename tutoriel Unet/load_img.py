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


noyeau_root = pathlib.Path(r'D:\DATA-USERS\Ambre Lamouchi\GitHub\stage-ENS-PLATIM-M1\tutoriel Unet\unet_img')
# print(noyeau_root)
# PIL.Image.open("./cell_nuclei_train_f_only/class1/0_t.png").show()

# print(type(train_masque))

# for item in noyeau_root.glob("*"):
#   print(item.name)


list_ds = tf.data.Dataset.list_files(str(noyeau_root/'img/*'))
list_dm = tf.data.Dataset.list_files(str(noyeau_root/'label/*'))

print(train_img)
print(list_ds)

# for f in list_ds.take(5):
#   print(f.numpy())

def process_path(file_path):
  label = tf.strings.split(file_path, os.sep)[-2]
  return tf.io.read_file(file_path), label

labeled_ds = list_ds.map(process_path)
labeled_dm = list_dm.map(process_path)

# print(list_ds)

# for image_raw, label_text in labeled_ds.take(1):
#   print(type(image_raw))
#   print()
#   print(label_text.numpy())

# # Reads an image from a file, decodes it into a dense tensor, and resizes it
# # to a fixed shape.

def parse_image(filename):
  parts = tf.strings.split(filename, os.sep)
  label = parts[-2]

  image = tf.io.read_file(filename)
  image = tf.image.decode_jpeg(image)
  image = tf.image.convert_image_dtype(image, tf.float32)
  image = tf.image.resize(image, [128, 128])
  return image, label


file_path = next(iter(list_ds))
file_path2 = next(iter(list_dm))

image, label = parse_image(file_path)
image2, label2 = parse_image(file_path2)

for element in list_ds.take(10).as_numpy_iterator():
  print(element)

def show(image, label):
  plt.figure()
  plt.imshow(image)
  plt.title(label.numpy().decode('utf-8'))
  plt.axis('off')
 

# print(len(image))

# show(image, label)
# show(image2, label2)

plt.show()

print("#########################################################")



# https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/image?hl=fr

# print(os.path.exists("./cell_nuclei_train_f_only/class1/"+"1.png"))
# print(os.path.exists("./cell_nuclei_train_f_only/class1/"+"0_t.png"))



# plt.figure(figsize=(15, 15))

# print("train = ",train_img)

# for i in range(0,1):
    
#     name_img = train_img.filenames[i].split("\\")[1]
#     masque_name_img = train_masque.filenames[i].split("\\")[1]

#     plt.subplot(1, 2, i+1)
#     plt.title("euhh")
#     img = PIL.Image.open("./cell_nuclei_train_f_only/class1/"+name_img)
#     masque_img = PIL.Image.open("./cell_nuclei_train_label_f_only/masque/"+masque_name_img)
    
#     print(type(img))
#     plt.imshow(img)
#     plt.axis('off')

#     plt.subplot(1, 2, i+2)
#     plt.title("euh2")
#     plt.imshow(masque_img)

#     plt.axis('off')

# plt.show()

# print(train_masque)


# print(len(train_it.classes))