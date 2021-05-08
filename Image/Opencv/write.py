import cv2


original_image = cv2.imread("images\\lion.jpg", cv2.IMREAD_UNCHANGED)
original_image = cv2.resize(original_image, (450,300))
# cv2.IMWRITE_JPEG_QUALITY值為0 ~ 100
cv2.imwrite("lion_output_jpg.jpg", original_image, [cv2.IMWRITE_JPEG_QUALITY, 10])
print("[INFO] lion_output_jpg.jpg has stored.")

# cv2.IMWRITE_PNG_COMPRESSION值為0 ~ 9
cv2.imwrite("lion_output_png.png", original_image, [cv2.IMWRITE_PNG_COMPRESSION, 5])
print("[INFO] lion_output_png.png has stored.")


output_jpg = cv2.imread("images\\lion_output_jpg.jpg")
output_png = cv2.imread("images\\lion_output_png.png")

# cv2.namedWindow("視窗名稱", cv2.WINDOW_NORMAL)，cv2.WINDOW_NORMAL讓視窗可以自由放大縮小，且圖像會跟著改變大小
cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
# 若是要同時使用cv2.namedWindow()和cv2.imshow()，則視窗名稱需要一致，才不會出現兩個視窗
cv2.imshow("Original", original_image)
cv2.namedWindow("Output_JPG", cv2.WINDOW_NORMAL)
cv2.imshow("Output_JPG", output_jpg)
cv2.namedWindow("Output_PNG", cv2.WINDOW_NORMAL)
cv2.imshow("Output_PNG", output_png)

cv2.waitKey(0)
cv2.destroyAllWindows()