import cv2
import numpy as np

from server_utils.image_utils import image_resize

face_cascade = cv2.CascadeClassifier('./server_utils/data/haarcascade_frontalface_default.xml')
eyes_cascade = cv2.CascadeClassifier('./server_utils/data/frontalEyes35x16.xml')
nose_cascade = cv2.CascadeClassifier('./server_utils/data/Nose18x15.xml')
glasses = cv2.imread("./server_utils/images/glasses2.png", -1)
mustache = cv2.imread('./server_utils/images/mustache.png', -1)


def glasses_stache(imagePath, rectangles):
    image = cv2.imread(imagePath)

    img = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + h]  # rec
        roi_color = img[y:y + h, x:x + h]
        if rectangles:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)

        eyes = eyes_cascade.detectMultiScale(roi_gray, scaleFactor=1.5, minNeighbors=5)
        for (ex, ey, ew, eh) in eyes:
            roi_eyes = roi_gray[ey: ey + eh, ex: ex + ew]

            if rectangles:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 3)

            else:
                glasses2 = image_resize(glasses.copy(), width=ew)
                gw, gh, gc = glasses2.shape
                for i in range(0, gw):
                    for j in range(0, gh):
                        # print(glasses[i, j]) #RGBA
                        if glasses2[i, j][3] != 0:  # alpha 0
                            roi_color[ey + i, ex + j] = glasses2[i, j]

        nose = nose_cascade.detectMultiScale(roi_gray, scaleFactor=1.5, minNeighbors=5)
        for (nx, ny, nw, nh) in nose:
            roi_nose = roi_gray[ny: ny + nh, nx: nx + nw]

            if rectangles:
                cv2.rectangle(roi_color, (nx, ny), (nx + nw, ny + nh), (0, 0, 255), 3)

            else:
                mustache2 = image_resize(mustache.copy(), width=nw)
                mw, mh, mc = mustache2.shape
                for i in range(0, mw):
                    for j in range(0, mh):
                        # print(glasses[i, j]) #RGBA
                        if mustache2[i, j][3] != 0:  # alpha 0
                            roi_color[ny + int(nh / 2.0) + i, nx + j] = mustache2[i, j]

    final_img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
    cv2.imwrite(imagePath, final_img)


if __name__ == "__main__":
    glasses_stache('images/face1-Copy.jpg', True)
