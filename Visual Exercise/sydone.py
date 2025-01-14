import cv2
import numpy as np
import os

def detect_corners(image_path):
    """
    检测定标板角点。

    Args:
        image_path (str): 定标板图像路径。

    Returns:
        list: 检测到的角点坐标列表。
    """

    # 加载图像
    if not os.path.exists(image_path):
        print(f"文件 {image_path} 不存在！")
        return []
    img = cv2.imread(image_path)

    # 转换为灰度图像
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 应用阈值分割，将图像转换为黑白
    ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # 使用轮廓查找
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 找到最大的轮廓，即定标板
    largest_contour = max(contours, key=cv2.contourArea)

    # 使用最小外接矩形近似轮廓
    x, y, w, h = cv2.boundingRect(largest_contour)

    # 获取矩形四个角点
    corners = [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]

    return corners

# 测试
image_path1 = "D:/robotest/pone.png"
image_path2 = "D:/robotest/ptwo.png"

corners1 = detect_corners(image_path1)
corners2 = detect_corners(image_path2)

print("图1 的角点坐标：", corners1)
print("图2 的角点坐标：", corners2)

# 可选：在图像上绘制角点
img1 = cv2.imread(image_path1)
img2 = cv2.imread(image_path2)
for corner in corners1:
    cv2.circle(img1, corner, 5, (0, 0, 255), -1)
for corner in corners2:
    cv2.circle(img2, corner, 5, (0, 0, 255), -1)

cv2.imshow("图1 的角点", img1)
cv2.imshow("图2 的角点", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()