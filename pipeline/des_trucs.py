import os
import random
import re
from PIL import Image

DATA_PATH = ''
FRAME_PATH = ''
MASK_PATH = ''


# Creat folders to hold images and masks

folders = ['train_frames', 'train_masks', 'val_frames', 'val_masks', 'test_frames', 'test_masks']
