# Usage
# python read_video_to_images.py -i F:/Master/Smart_door_system/Dataset/Face/Michael/Michael.mov -o F:/Master/Smart_door_system/Dataset/Face/Michael/Original_image/ -c 1

import cv2
import argparse

def greatest_common_factor(a, b):
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return int(a)

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required = True, help = "Input video path.")
ap.add_argument("-o", "--output", required = True, help = "Output images path.")
ap.add_argument("-c", "--catch_freq", required = True, default=1, help = "Grab every x frames.")
args = vars(ap.parse_args())

video_images = []
vc = cv2.VideoCapture(args["input"])
catch_freq = int(args["catch_freq"])
num = 1

#判斷是否開啟影片
assert vc.isOpened(), "Can't not init video..., you need to check your video path."

# 取得影片的資訊
video_width = vc.get(cv2.CAP_PROP_FRAME_WIDTH)
video_height = vc.get(cv2.CAP_PROP_FRAME_HEIGHT)
video_rate = vc.get(cv2.CAP_PROP_FPS)
video_total_frames = vc.get(cv2.CAP_PROP_FRAME_COUNT)

print("[INFO] video width : %d pixs" % video_width)
print("[INFO] video height: %d pixs" % video_height)
print("[INFO] video rate  : %.2f fps" % video_rate)
print("[INFO] Total frame : %d frame" % video_total_frames)

# 計算兩數的最大公因數
greatest_common_factor = greatest_common_factor(video_width, video_height)

video_width = int(video_width / greatest_common_factor  * 50)
video_height = int(video_height / greatest_common_factor * 50)

while True:
    try:
        # 讀取單個幀的影像
        status, video_frame = vc.read()

        # 0 = 垂直翻轉，1 = 水平翻轉， < 0 = 同時水平與垂直翻轉 
        video_frame = cv2.flip(video_frame, 0)

        if type(video_frame) == type(None):
            break

        elif(vc.get(cv2.CAP_PROP_POS_FRAMES) % catch_freq == 0): #每隔幾幀進行擷取
            video_images.append(video_frame)
            cv2.imwrite(args["output"] + str(num).zfill(5) + ".jpg", video_frame)
            cv2.imshow('windows', cv2.resize(video_frame, (video_width, video_height)))
            cv2.waitKey(24)
            num += 1
            print("\r\b[INFO] Catch image count: " ,num, end ="")
    except KeyboardInterrupt as err:
        print("\n[ERROR] Keyboard interrupt !")
        vc.release()
        cv2.destroyAllWindows
        break
    except cv2.error as err:
        print("\n[ERROR] Error message: %s" % err)
        vc.release()
        cv2.destroyAllWindows
        break

vc.release()
cv2.destroyAllWindows
print("\n[INFO] Finish read video to images.")


# 參考: 
# http://cvfiasd.pixnet.net/blog/post/270018236-%E8%AE%80%E5%8F%96%E5%BD%B1%E7%89%87%E4%B8%A6%E8%BD%89%E6%88%90%E5%9C%96%E7%89%87
# https://blog.csdn.net/yuejisuo1948/article/details/80734908
# https://docs.opencv.org/4.0.0/d4/d15/group__videoio__flags__base.html#ggaeb8dd9c89c10a5c63c139bf7c4f5704da7c2fa550ba270713fca1405397b90ae0