import cv2 as cv
import numpy as np

def get_image_area_pix(x_start = int(), x_end = int(), y_start = int(),
                        y_end = int(), image_path = str()):
    img = cv.imread(image_path)
    if type(img) != None:
        img = img[x_start:x_end, y_start:y_end]
        cv.imshow("Frame", img)
        cv.waitKey(0)
        cv.destroyAllWindows()
    else:
        print("Not found image!") 


def edit_image_area_pix(x_start = int(), x_end = int(), y_start = int(),
                        y_end = int(), image_path = str(), pix_value = int()):
    img = cv.imread(image_path)
    if type(img) != None:        
        img = img.copy()
        ROI = img[x_start:x_end, y_start:y_end]
        for i in range(3):
            ROI[:,:,i] = pix_value

        img[x_start:x_end, y_start:y_end] = ROI
        cv.imshow("Frame", img)
        cv.waitKey(0)
        cv.destroyAllWindows()
    else:
        print("Not found image!") 


# channel range is 0 ~ 2, B、G、R channels. 
def get_image_one_pix(x = int(), y = int(), image_path = str(), channel = 0):
    img = cv.imread(image_path)
    if type(img) != None:
        print("[INFO] pix is: ",img.item(x, y, channel))
    else:
        print("Not found image!")

def edit_image_one_pix(x = int(), y = int(), pix_value = int(), image_path = str(), channel = 0):
    img = cv.imread(image_path)
    if type(img) != None:
        img = cv.imread(image_path)
        img = img.copy()
        print("[INFO] Original pix is: %d" % img.item(x, y, channel))
        img.itemset(x, y, channel, pix_value)
        print("[INFO] After edit pix is: ",img.item(x, y, channel))
    else:
        print("Not found image!") 


def print_image_information(image_path = str()):
    img = cv.imread(image_path)
    if type(img) != None:
        print("[INFO] Image data type: ", img.dtype)
        print("[INFO] Image shape    : ", img.shape)
        print("[INFO] Image dimension: ", img.ndim)
        print("[INFO] Image size(width*height*channels): ", img.size)
    else:
        print("Not found image!") 