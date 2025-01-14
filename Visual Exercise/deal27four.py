import cv2
import numpy as np

# 加载图像
img = cv2.imread(r"D:\waterbot\four.png")  # 使用原始字符串

# 将图像转换为灰度图像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 阈值化，将黑色海胆区域设置为白色，其他区域设置为黑色
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

# 定义腐蚀核
kernel = np.ones((5, 5), np.uint8)

# 腐蚀图像
erosion = cv2.erode(thresh, kernel, iterations=1)

# 膨胀图像
dilation = cv2.dilate(erosion, kernel, iterations=1)

# 显示结果
cv2.imshow("Original", img)
cv2.imshow("Thresh", thresh)
cv2.imshow("Erosion", erosion)
cv2.imshow("Dilation", dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()