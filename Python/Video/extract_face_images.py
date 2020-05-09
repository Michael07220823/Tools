# Usage
# python extra_face_images.py -i videos\Trump.mp4 -o extract_images -f 0
# python extra_face_images.py -i 0 -o extract_images -f 0

import cv2
import sys
import time
import argparse

    
def detectFaceOpenCVDnn(net, frame):
    frameOpencvDnn = frame.copy()
    frameHeight = frameOpencvDnn.shape[0]
    frameWidth = frameOpencvDnn.shape[1]
    blob = cv2.dnn.blobFromImage(frameOpencvDnn, 1.0, (300, 300), [104, 117, 123], False, False)

    net.setInput(blob)
    detections = net.forward()
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > conf_threshold:
            x = int(detections[0, 0, i, 3] * frameWidth)
            y = int(detections[0, 0, i, 4] * frameHeight)
            w = int(detections[0, 0, i, 5] * frameWidth)
            h = int(detections[0, 0, i, 6] * frameHeight)
            bboxes = [x, y, w, h]
            cv2.rectangle(frameOpencvDnn, (x, y), (w, h), (0, 255, 0), int(round(frameHeight/150)), 8)

            # Save image
            cv2.imwrite(args["output"] + "\\{}.jpg".format(str(frame_count).zfill(5)), frame[y:h, x:w])
        else:
            bboxes = None
    return frameOpencvDnn, bboxes


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True, help="Input video path or device index like 0.")
ap.add_argument("-o", "--output", required=True, help="Output images path.")
ap.add_argument("-f", "--flip", required=False, help="Flip frame.")
args = vars(ap.parse_args())

# OpenCV DNN supports 2 networks.
# 1. FP16 version of the original caffe implementation ( 5.4 MB )
# 2. 8 bit Quantized version using Tensorflow ( 2.7 MB )
DNN = "TF"
if DNN == "CAFFE":
    modelFile = "models/face_detection/res10_300x300_ssd_iter_140000_fp16.caffemodel"
    configFile = "models/face_detection/deploy.prototxt"
    net = cv2.dnn.readNetFromCaffe(configFile, modelFile)
else:
    modelFile = "models/face_detection/opencv_face_detector_uint8.pb"
    configFile = "models/face_detection/opencv_face_detector.pbtxt"
    net = cv2.dnn.readNetFromTensorflow(modelFile, configFile)

conf_threshold = 0.7

if not args["input"].isdigit():
    cap = cv2.VideoCapture(args["input"])
else:
    cap = cv2.VideoCapture(int(args["input"]))

hasFrame, frame = cap.read()


frame_count = 0
tt_opencvDnn = 0

while cap.isOpened():
    hasFrame, frame = cap.read()

    # Get video information
    video_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    video_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

    frame = cv2.flip(cv2.resize(frame, (800, 450)), int(args["flip"]))

    if not hasFrame:
        break
    frame_count += 1

    t = time.time()
    outOpencvDnn, bboxes = detectFaceOpenCVDnn(net, frame)

    tt_opencvDnn += time.time() - t
    fpsOpencvDnn = frame_count / tt_opencvDnn
    label = "OpenCV DNN ; FPS : {:.2f}".format(fpsOpencvDnn)
    cv2.putText(outOpencvDnn, label, (10,50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow("Face Detection Comparison", outOpencvDnn)

    if frame_count == 1:
        tt_opencvDnn = 0

    k = cv2.waitKey(10) & 0xFF
    if k == ord("q"):
        cap.release()
        cv2.destroyAllWindows()
        break
