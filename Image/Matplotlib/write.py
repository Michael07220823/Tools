from matplotlib import pyplot as plt 

image = plt.imread("images\\lion.jpg")
plt.imshow(image)
# 關閉XY軸座標
plt.axis("off")
# 儲存圖像，savefig()須放於show()前面，不須要指定變數名稱
plt.savefig("images\\lion_output.jpg")
plt.show()