# Usage
# python face_detect.py -i images\Lenna.jpg -haar haarcascade\haarcascade_frontalface_default.xml
import os
import sys
import argparse
import cv2 as cv
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Input image path.")
ap.add_argument("-haar", "--haarcascade_path", required=True, help="Input haarcascade path.")
args = vars(ap.parse_args())


if os.path.exists(args["image"]):
    dir_path = os.path.splitext(args["image"])[0]
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

    img = cv.imread(args["image"])
    face_cascade = cv.CascadeClassifier(args["haarcascade_path"])

    faces = face_cascade.detectMultiScale(img,
                                          scaleFactor = 1.01,
                                          minNeighbors = 12,
                                          minSize = (15, 15),
                                          maxSize= (200, 200)
    )
    
    if type(faces) != tuple:
        if len(faces) > 1:
            count = 0
            for x, y, w, h in faces:
                count += 1
                face = img[y:y+h, x:x+w]
                img_path = os.path.join(dir_path, os.path.split(dir_path)[-1] + "_roi_" + str(count) + os.path.splitext(args["image"])[1])
                cv.imwrite(img_path, face)
        else:
            for x, y, w, h in faces:
                face = img[y:y+h, x:x+w]
                img_path = os.path.join(dir_path, os.path.split(dir_path)[-1] + "_roi" + os.path.splitext(args["image"])[1])
                cv.imwrite(img_path, face)

    cv.imshow("Face", face)
    cv.imshow("Original", img)

    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print("[Error] Image path error !")
