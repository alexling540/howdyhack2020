import cv2
import numpy as np

from utils import image_resize

face_cascade = cv2.CascadeClassifier('venv/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('venv/Lib/site-packages/cv2/data/frontalEyes35x16.xml')
nose_cascade = cv2.CascadeClassifier('venv/Lib/site-packages/cv2/data/Nose18x15.xml')

img = cv2.imread('images/face1.jpg')
glasses = cv2.imread("images/glasses2.png")
mustache = cv2.imread('images/mustache.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 3)

for (x, y, w, h) in faces:
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    roi_gray = gray[y:y + h, x:x + w]
    roi_color = img[y:y + h, x:x + w]

    eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.5, minNeighbors=5)
    for (ex, ey, ew, eh) in eyes:
        # cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
        roi_eyes = roi_gray[ey: ey + eh, ex: ex + ew]
        glasses2 = image_resize(glasses.copy(), width=ew)

        gw, gh, gc = glasses2.shape
        for i in range(0, gw):
            for j in range(0, gh):
                #print(glasses[i, j]) #RGBA
                if glasses2[i, j][2] != 0:  # alpha 0
                    roi_color[ey + i, ex + j] = glasses2[i, j]

    nose = nose_cascade.detectMultiScale(roi_gray, scaleFactor=1.5, minNeighbors=10)
    for (nx, ny, nw, nh) in nose:
        cv2.rectangle(roi_color, (nx, ny), (nx + nw, ny + nh), (0, 0, 255), 2)
        roi_nose = roi_gray[ny: ny + nh, nx: nx + nw]
        mustache2 = image_resize(mustache.copy(), width=nw)

        mw, mh, mc = mustache2.shape
        for i in range(0, mw):
            for j in range(0, mh):
                #print(mustache2[i, j][3]) #RGBA
                if mustache2[i, j][2] != 0:  # alpha 0
                    roi_color[ny + int(nh/2.0) + i, nx + j] = mustache2[i, j]

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
