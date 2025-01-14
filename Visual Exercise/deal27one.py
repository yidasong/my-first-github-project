import numpy as np
import cv2
import matplotlib.pyplot as plt

# 读取图片
img = cv2.imread("D:/waterbot/one.png", cv2.IMREAD_COLOR)  # 使用 IMREAD_COLOR 读取彩色图像

# 添加噪声
img_noise = img.copy()  # 复制图像，避免修改原图像
rows, cols, chn = img_noise.shape
for i in range(5000):
    x = np.random.randint(0, rows)
    y = np.random.randint(0, cols)
    img_noise[x, y, :] = 255

# 转换颜色空间
img_noise = cv2.cvtColor(img_noise, cv2.COLOR_BGR2RGB)  # 将 BGR 转换为 RGB

# 显示图片
plt.figure(figsize=(10, 10))
plt.imshow(img_noise)
plt.axis('off')  # 关闭坐标轴
plt.show()

# 保存图片
cv2.imwrite("D:/waterbot/one_noise.png", cv2.cvtColor(img_noise, cv2.COLOR_RGB2BGR))  # 保存时转换回 BGR