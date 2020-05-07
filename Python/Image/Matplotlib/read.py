import matplotlib.pyplot as plt 

image = plt.imread("images\\lion.jpg")
print("[INFO] Image shape: ", image.shape)

plt.imshow(image)
# 關閉XY軸座標
plt.axis("off")
plt.show()