import os
import random
import re
from PIL import Image

DATA_PATH = ''
FRAME_PATH = ''
MASK_PATH = ''

from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)
        
val_datagen = ImageDataGenerator(rescale=1./255)

# Creat folders to hold images and masks
train_image_generator = train_datagen.flow_from_directory('./data/train_frames/',batch_size = 32)

train_mask_generator = train_datagen.flow_from_directory('./data/train_masks/',batch_size = 32)

val_image_generator = val_datagen.flow_from_directory('./data/val_frames/',batch_size = 32)


val_mask_generator = val_datagen.flow_from_directory( './data/val_masks/',batch_size = 32)

print(val_mask_generator.filenames)

train_generator = zip(train_image_generator, train_mask_generator)
val_generator = zip(val_image_generator, val_mask_generator)