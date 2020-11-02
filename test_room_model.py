# import the necessary packages
import time

from imutils.video import WebcamVideoStream
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from imutils import build_montages
from imutils import paths
import numpy as np
import argparse
import random
import cv2


# load the pre-trained network
print("[INFO] loading pre-trained network...")
model = load_model('floorModel')

# grab all image paths in the input directory and randomly sample them
video_src = 'http://192.168.1.15:8080/video'
_video_stream = WebcamVideoStream(video_src).start()
# allow the camera to warm up
time.sleep(2.0)
i = 1
while i < 100000:
    orig = _video_stream.read()
    orig = cv2.flip(orig, 0)
    if orig is None:
        break
    frame = cv2.resize(orig, (64, 64))
    frame = frame.astype("float") / 255.0
    i+=1
    frame = img_to_array(frame)
    frame = np.expand_dims(frame, axis=0)
    # make predictions on the input image
    pred = model.predict(frame)
    pred = pred.argmax(axis=1)[0]
    # an index of zero is the 'parasitized' label while an index of
    # one is the 'uninfected' label
    label = "above" if pred == 0 else "bounds" if pred == 1 else "floor"
    color = (0, 0, 255) if pred == 0 else (0, 255, 0) if pred == 1 else (255, 0, 0)
    # resize our original input (so we can better visualize it) and
    # then draw the label on the image
    cv2.putText(orig, label, (3, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                color, 2)

    cv2.imshow("Results", orig)
    cv2.waitKey(1)