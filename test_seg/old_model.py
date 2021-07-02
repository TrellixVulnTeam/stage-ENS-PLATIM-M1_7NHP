from keras_preprocessing.image import directory_iterator
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

from keras.preprocessing.image import ImageDataGenerator
from tensorflow.python import keras
# from keras import utils as np_utils
from keras.utils import np_utils
from keras_segmentation.pretrained import pspnet_50_ADE_20K , pspnet_101_cityscapes, pspnet_101_voc12
# import tensorflow.python.keras.utils.generic_utils


train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)
        
val_datagen = ImageDataGenerator(rescale=1./255)

train_image_generator = train_datagen.flow_from_directory( 'data/train_frames')

train_mask_generator = train_datagen.flow_from_directory( 'data/train_masks')

val_image_generator = val_datagen.flow_from_directory( 'data/val_frames')

val_mask_generator = val_datagen.flow_from_directory( 'data/val_masks')

# , batch_size = 16



train_generator = zip(train_image_generator, train_mask_generator)
val_generator = zip(val_image_generator, val_mask_generator)

print(type(train_image_generator))
# set(zip(train_image_generator, train_mask_generator))

# print(set(train_generator))
import cv2
import random

def data_gen(img_folder, mask_folder, batch_size):
  c = 0
  n = os.listdir(img_folder) #List of training images
  random.shuffle(n)
  
  while (True):
    img = np.zeros((batch_size, 512, 512, 3)).astype('float')
    mask = np.zeros((batch_size, 512, 512, 1)).astype('float')

    for i in range(c, c+batch_size): #initially from 0 to 16, c = 0. 

      train_img = cv2.imread(img_folder+'/'+n[i])/255.
      train_img =  cv2.resize(train_img, (512, 512))# Read an image from folder and resize
      
      img[i-c] = train_img #add to array - img[0], img[1], and so on.
                                                   

      train_mask = cv2.imread(mask_folder+'/'+n[i], cv2.IMREAD_GRAYSCALE)/255.
      train_mask = cv2.resize(train_mask, (512, 512))
      train_mask = train_mask.reshape(512, 512, 1) # Add extra dimension for parity with train_img size [512 * 512 * 3]

      mask[i-c] = train_mask

    c+=batch_size
    if(c+batch_size>=len(os.listdir(img_folder))):
      c=0
      random.shuffle(n)
                  # print "randomizing again"
    yield img, mask



train_frame_path_img = './data/train_frames/train/mask_0.png'

train_frame_path = './data/train_frames/train'
train_mask_path = './data/train_masks/train'

val_frame_path = './data/val_frames/val'
val_mask_path = './data/val_masks/val'

# Train the model
train_gen = data_gen(train_frame_path,train_mask_path, batch_size = 4)
val_gen = data_gen(val_frame_path,val_mask_path, batch_size = 4)

print(type(train_gen))



model = pspnet_101_voc12()
# model = pspnet_101_cityscapes()