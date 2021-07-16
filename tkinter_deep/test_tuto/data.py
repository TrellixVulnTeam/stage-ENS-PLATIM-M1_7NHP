import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import tensorflow as tf
import cv2
from PIL import Image

import matplotlib.pyplot as plt

H = 256
W = 256

label = ["frame", "mask"]

def read_image(x):
    x = cv2.imread(x, cv2.IMREAD_GRAYSCALE) 
    # cv2.IMREAD_COLOR)
    x = cv2.resize(x, (W, H))
    x = x / 255.0
    x = x.astype(np.float32)
    return x


def load_data_2_class():
    test_frames = os.listdir("data_2/test_frames/")
    test_masks = os.listdir("data_2/test_masks/")
    train_frames = os.listdir("data_2/train_frames/train/")
    train_masks = os.listdir("data_2/train_masks/train/")

    val_frames = os.listdir("data_2/val_frames/val/")
    val_masks = os.listdir("data_2/val_masks/val/")

    train_x = []
    train_y = []

    train_t = []
    test_t = []


    label_train = []

    valid_x = []
    valid_y = []
    test_x = [] 
    test_y = []

    label_test = []



    np_test_frames = np.array(test_frames)

    for i in range(0,len(test_frames)):
        # test_x.append("data_2/test_frames/"+test_frames[i])
        # test_y.append("data_2/test_masks/"+test_masks[i])
        test_t.append("data_2/test_frames/"+test_frames[i])
        test_t.append("data_2/test_masks/"+test_masks[i])

        label_test.append(0)
        label_test.append(1)



    for i in range(0,len(train_frames)):
        # train_x.append("data_2/train_frames/train/"+train_frames[i])
        # train_y.append("data_2/train_masks/train/"+train_masks[i])
        train_t.append("data_2/train_frames/train/"+train_frames[i])
        train_t.append("data_2/train_masks/train/"+train_masks[i])
        
        label_train.append(0)
        label_train.append(1)

    train_t = np.array(train_t)
    test_t = np.array(test_t)

    # train_x, valid_x = train_test_split(train_x, test_size=0.2, random_state=42)
    # train_y, valid_y = train_test_split(train_y, test_size=0.2, random_state=42)

    return (train_t, label_train), (test_t, label_test)


def plot_image(i, predictions_array, true_label, img):
  true_label, img = true_label[i], img[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])

  plt.imshow(img, cmap=plt.cm.binary)

  predicted_label = np.argmax(predictions_array)
  if predicted_label == true_label:
    color = 'blue'
  else:
    color = 'red'

  plt.xlabel("{} {:2.0f}% ({})".format(label[predicted_label],
                                100*np.max(predictions_array),
                                label[true_label]),
                                color=color)


def plot_value_array(i, predictions_array, true_label):
  true_label = true_label[i]
  plt.grid(False)
  plt.xticks(range(2))
  plt.yticks([])
  thisplot = plt.bar(range(2), predictions_array, color="#777777")
  plt.ylim([0, 1])
  predicted_label = np.argmax(predictions_array)

  thisplot[predicted_label].set_color('red')
  thisplot[true_label].set_color('blue')


if __name__ == "__main__":
    print("coucou")
    (train_t, label_train), (test_t, label_test) = load_data_2_class()

    print(train_t[0])

    train_t2 = np.array(list(map(read_image, train_t)))
    test_t2 = np.array(list(map(read_image, test_t)))
    # print(train_t2[0])

    # print(train_t2[0])

    print(train_t2.shape)

    model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(256, 256)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(2)
    ])

    model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])


    model.fit(train_t2, np.array(label_train), epochs=10)

    probability_model = tf.keras.Sequential([model, 
                                         tf.keras.layers.Softmax()])
    
    predictions = probability_model.predict(test_t2)
    print(test_t[0])
    print(predictions[0])

    i = 0
    plt.figure(figsize=(6,3))
    plt.subplot(1,2,1)
    plot_image(i, predictions[i], label_test, test_t2)
    plt.subplot(1,2,2)
    plot_value_array(i, predictions[i],  label_test)
    plt.show()
