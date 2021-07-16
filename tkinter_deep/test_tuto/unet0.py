from tensorflow.keras.layers import *
from tensorflow.keras.models import model_from_config

def conv_block(inputs, num_filters):
    x = Conv2D(num_filters, 3, padding="same")(inputs)
    x = BatchNormalization()(x)
    x = Activation("relu")(x)

    x = Conv2D(num_filters, 3, padding="same")(inputs)
    x = BatchNormalization()(x)
    x = Activation("relu")(x)

    return x

def encoder_block(inputs, num_filters):
    x = conv_block(inputs, num_filters)
    p = MaxPool2D((2,2))(x)

    return x, p

def decorder_block(inputs, skip_features, num_filters):
    x = Conv2DTranspose(num_filters, (2,2), strides = 2, padding='same')(inputs)
    