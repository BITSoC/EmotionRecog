# -*- coding: utf-8 -*-
"""emotion_recog_mobilenetv2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1a0lgJIuXquWwYj1Bw9WfQbfT2mwjV_8N
"""

from google.colab import drive
drive.mount('/content/gdrive',force_remount=True)

"""# Imported importanat libraries"""

# baseline model with dropout and data augmentation on the cifar10 dataset
import sys
import tensorflow
from matplotlib import pyplot
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential,Model
from tensorflow.keras.layers import Conv2D,MaxPooling2D,Dense,Flatten,Dropout,BatchNormalization,AveragePooling2D
from tensorflow.keras.optimizers import SGD,Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import load_img
from imutils import paths
import matplotlib.pyplot as plt
import numpy as np
import random
import os

"""# Preprocessing of image and labels"""

data_train = '/content/gdrive/My Drive/emotion_recog/emo'

imagepaths = list(paths.list_images(data_train))
random.shuffle(imagepaths)
random.seed(42)

# visualisation
x = [random.randint(0, len(imagepaths)) for p in range(0, 9)]
for p,i in enumerate(x):
	# define subplot
	plt.subplot(330 + 1 + p)
	# plot raw pixel data
	image = load_img(imagepaths[i],(224,224))
	plt.imshow(image)

# preprocessing

data_images = []
labels = []
for imgpath in imagepaths:
	label = imgpath.split(os.path.sep)[-2]
	img = load_img(imgpath, target_size=(224, 224))
	data_images.append(img_to_array(img)/255.)
	labels.append(label)

# encoding label name into value
# converting data and label to array
from sklearn.preprocessing import LabelEncoder
lb = LabelEncoder()
labels_z = lb.fit_transform(np.array(labels))
labels_value = to_categorical(labels_z,num_classes=6)
data = np.array(data_images,dtype='float32')

# storing preprocessed images and labels for further use
np.save('/content/gdrive/My Drive/emotion_recog/data.npy',data)
np.save('/content/gdrive/My Drive/emotion_recog/labels_value.npy',labels_value)

