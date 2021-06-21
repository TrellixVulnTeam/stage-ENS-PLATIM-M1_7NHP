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

from keras.callbacks import ModelCheckpoint
from keras.callbacks import CSVLogger
from keras.callbacks import EarlyStopping
from tensorflow.keras.optimizers import Adam

import os 
import model

####################################################

train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)
        
val_datagen = ImageDataGenerator(rescale=1./255)

train_image_generator = train_datagen.flow_from_directory( './data/train_frames', batch_size = 16)

train_mask_generator = train_datagen.flow_from_directory( './data/train_masks', batch_size = 16)

val_image_generator = val_datagen.flow_from_directory( './data/val_frames', batch_size = 16)


val_mask_generator = val_datagen.flow_from_directory( './data/val_masks', batch_size = 16)


####################################################
train_generator = zip(train_image_generator, train_mask_generator)
val_generator = zip(val_image_generator, val_mask_generator)
NO_OF_TRAINING_IMAGES = len(os.listdir('./data/train_frames/train/'))
NO_OF_VAL_IMAGES = len(os.listdir('./data/val_frames/val/'))

NO_OF_EPOCHS = 30

BATCH_SIZE = 16

weights_path = 'path/where/resulting_weights_will_be_saved'

m = model.unet()
opt = Adam(lr=1E-5, beta_1=0.9, beta_2=0.999, epsilon=1e-08)

m.compile(loss=None,
              optimizer=opt,
              metrics=None)

checkpoint = ModelCheckpoint(weights_path, monitor='METRIC_TO_MONITOR', 
                             verbose=1, save_best_only=True, mode='max')

csv_logger = CSVLogger('./log.out', append=True, separator=';')

earlystopping = EarlyStopping(monitor = 'METRIC_TO_MONITOR', verbose = 1,
                              min_delta = 0.01, patience = 3, mode = 'max')

callbacks_list = [checkpoint, csv_logger, earlystopping]

results = m.fit_generator(train_gen, epochs=NO_OF_EPOCHS, 
                          steps_per_epoch = (NO_OF_TRAINING_IMAGES//BATCH_SIZE),
                          validation_data=val_gen, 
                          validation_steps=(NO_OF_VAL_IMAGES//BATCH_SIZE), 
                          callbacks=callbacks_list)
m.save('Model.h5')