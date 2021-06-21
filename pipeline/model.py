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

train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)
        
val_datagen = ImageDataGenerator(rescale=1./255)

train_image_generator = train_datagen.flow_from_directory( 'data/train_frames/train', batch_size = 16)

train_mask_generator = train_datagen.flow_from_directory( 'data/train_masks/train', batch_size = 16)

val_image_generator = val_datagen.flow_from_directory( 'data/val_frames/val', batch_size = 16)


val_mask_generator = val_datagen.flow_from_directory( 'data/val_masks/val', batch_size = 16)



train_generator = zip(train_image_generator, train_mask_generator)
val_generator = zip(val_image_generator, val_mask_generator)