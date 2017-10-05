print('Load the packages...')

import tensorflow as tf
import keras
import numpy as np
import cv2
from threading import Thread
import matplotlib.pyplot
from matplotlib import pyplot as plt

from gtts import gTTS
import pygame

#import pylab

#matplotlib.use('TKAgg')

from imagenet import create_readable_names_for_imagenet_labels



def get_image_webcam():
    cam = cv2.VideoCapture(0)
    print('Please use "Enter" to capture or "Escape" to close.')

    cv2.namedWindow("Capture")

    while True:
        ret, frame = cam.read()
        cv2.imshow("test", frame)
        if not ret:
            break
        k = cv2.waitKey(1)

        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            frame = None
            break
        elif k%256 == 32 or k%256 == 13:
            # SPACE pressed
            break


    cam.release()

    cv2.destroyAllWindows() 
    return frame


print('Load the inception network... ')


inception = keras.applications.inception_v3.InceptionV3(
    include_top=True, weights='imagenet', input_tensor=None, input_shape=None, pooling=None, classes=1000)

print('Load the labels... ')
names = create_readable_names_for_imagenet_labels()


print('Aquire an image...')
img = get_image_webcam()

while not(img is None):
    print('Resize the image...')

    with tf.Session() as sess:
        img = np.expand_dims(img[:, :, [2, 1, 0]], axis = 0)
        img_small = tf.image.resize_images(
            img / 255, [299, 299 * img.shape[2] // img.shape[1]])
        img_resize = tf.image.resize_image_with_crop_or_pad(
            img_small, 299, 299).eval()

    print('Classify the image...')
    probabilities = inception.predict(img_resize)[0,:]
    print('Display the results...')
    sorted_inds = [i[0] for i in sorted(enumerate(-probabilities), key=lambda x:x[1])]
    pred = []
    for i in range(5):
        index = sorted_inds[i]
        pred.append('Probability %0.2f%% => [%s]' % (probabilities[index], names[index+1]))
    
    # fig = pylab.figure()
    # pylab.gca().set_position((.1, .3, .8, .6)) # to make a bit of room for extra text
    # pylab.imshow(np.reshape(img_resize,[299,299,3]))
    # pylab.axis('off')
    # pylab.figtext(.02, .02, '\n'.join(pred))
    # pylab.draw()
    # pylab.waitforbuttonpress()
    # pylab.close(fig)
    tts = gTTS(text='This is a ' + names[sorted_inds[0]+1], lang='en')
    tts.save("sound.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("sound.mp3")
    pygame.mixer.music.play()

    fig = plt.figure()
    plt.gca().set_position((.1, .3, .8, .6)) # to make a bit of room for extra text
    plt.imshow(np.reshape(img_resize,[299,299,3]))
    plt.axis('off')
    plt.figtext(.02, .02, '\n'.join(pred))
    plt.draw()
    plt.waitforbuttonpress()
    plt.close(fig)

    while pygame.mixer.music.get_busy() == True:
        continue

    print('Aquire an image...')
    img = get_image_webcam()
