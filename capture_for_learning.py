import time

import cv2
import imutils
from imutils.video import WebcamVideoStream

video_src = 'http://192.168.1.15:8080/video'
_video_stream = WebcamVideoStream(video_src).start()
# allow the camera to warm up
time.sleep(2.0)
i = 1
while i < 1000:
    img = cv2.imread('data/' + str(i) + '.png', cv2.IMREAD_UNCHANGED)
    img = cv2.resize(img, (64,64), interpolation=cv2.INTER_AREA)
    print(cv2.imwrite('data-resized/' + str(i) + '.png', img))
    # frame = _video_stream.read()
    # if frame is None:
    #     break
    # frame = cv2.flip(frame, 0)
    # frame = imutils.resize(frame, width=128, height=128)
    # print(cv2.imwrite('data/' + str(i) + '.png', frame))
    # time.sleep(0.1)
    i+=1