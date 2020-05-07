import cv2 

# cv2.IMREAD_UNCHANGED 顏色比cv2.IMREAD_COLOR還要鮮豔
image1 = cv2.imread("images\\lion.jpg", cv2.IMREAD_UNCHANGED)

print("[INFO] Original lion.jpg type: ", type(image1))
print("[INFO] Original lion.jpg's shape: ", image1.shape)
image1 = cv2.resize(image1, (450,300))

print("[INFO] Resize height to 300, width to 450, and shape is: ", image1.shape)
cv2.imshow("Imread unchanged", image1)

# cv2.IMREAD_COLOR 顏色比原檔淡一點
image2 = cv2.imread("images\\lion.jpg", cv2.IMREAD_COLOR)
image2 = cv2.resize(image2, (450,300))
cv2.imshow("Imread color", image2)

# cv2.IMREAD_GRAYSCALE 灰階
image3 = cv2.imread("images\\lion.jpg", cv2.IMREAD_GRAYSCALE)
image3 = cv2.resize(image3, (450,300))
cv2.imshow("Imread grayscale", image3)

cv2.waitKey(0)
cv2.destroyAllWindows()

# 參考:https://docs.opencv.org/4.1.0/d4/da8/group__imgcodecs.html