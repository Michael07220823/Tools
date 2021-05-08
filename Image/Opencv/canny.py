import cv2 

# 定義cv2.createTrackbar()裡的觸發函式
def nothing(x):     
    pass 

img_noblur = cv2.imread('images\\badminton.jpg')
img_noblur = cv2.resize(img_noblur, (960,640))
# 平均模糊，設定矩陣為7*7的大小
img = cv2.blur(img_noblur, (7,7))
# cv2.Canny(圖像變數, 最小值,最大值)，Canny邊緣檢測參考:https://docs.opencv.org/4.1.0/d7/de1/tutorial_js_canny.html
canny_edge = cv2.Canny(img, 0,0)
# 若是要同時使用cv2.namedWindow()和cv2.imshow()，則視窗名稱需要一致，才不會出現兩個視窗
cv2.namedWindow("Image", cv2.WINDOW_GUI_NORMAL)
cv2.imshow('Image', img) 
cv2.namedWindow("Canny edge", cv2.WINDOW_GUI_NORMAL)
cv2.imshow('Canny edge', canny_edge)   
# cv2.createTrackbar('標籤名稱','視窗名稱', 最小值,最大值, 觸發函式) 創建一個軌道滑動並將其附加到指定的視窗。
cv2.createTrackbar('min_value','Canny edge', 0,400, nothing) 
cv2.createTrackbar('max_value','Canny edge', 0,400, nothing) 

while(True):
    cv2.imshow('Image', img)
    cv2.imshow('Canny edge', canny_edge)
    # cv2.getTrackbarPos('標籤名稱', '視窗名稱')取得軌道目前的數值，用以控制Canny邊緣檢測的最小、最大值
    min_value = cv2.getTrackbarPos('min_value', 'Canny edge')
    max_value = cv2.getTrackbarPos('max_value', 'Canny edge')
    canny_edge = cv2.Canny(img, min_value,max_value)
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        cv2.destroyAllWindows()