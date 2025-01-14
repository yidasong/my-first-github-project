import cv2
import matplotlib.pyplot as plt

# 读取带噪声图片
img_noise = cv2.imread("D:/waterbot/one_noise.png")

# 原图
plt.subplot(2, 3, 1)
plt.imshow(cv2.cvtColor(img_noise, cv2.COLOR_BGR2RGB))
plt.title("Original")

# 3×3 𝜎=0.1
blurred_3_01 = cv2.GaussianBlur(img_noise, (3, 3), 0.1)
plt.subplot(2, 3, 2)
plt.imshow(cv2.cvtColor(blurred_3_01, cv2.COLOR_BGR2RGB))
plt.title("3x3, σ=0.1")

# 3×3 𝜎=1.0
blurred_3_10 = cv2.GaussianBlur(img_noise, (3, 3), 1.0)
plt.subplot(2, 3, 3)
plt.imshow(cv2.cvtColor(blurred_3_10, cv2.COLOR_BGR2RGB))
plt.title("3x3, σ=1.0")

# 7×7 𝜎=0.1
blurred_7_01 = cv2.GaussianBlur(img_noise, (7, 7), 0.1)
plt.subplot(2, 3, 4)
plt.imshow(cv2.cvtColor(blurred_7_01, cv2.COLOR_BGR2RGB))
plt.title("7x7, σ=0.1")

# 7×7 𝜎=1.0
blurred_7_10 = cv2.GaussianBlur(img_noise, (7, 7), 1.0)
plt.subplot(2, 3, 5)
plt.imshow(cv2.cvtColor(blurred_7_10, cv2.COLOR_BGR2RGB))
plt.title("7x7, σ=1.0")

plt.tight_layout()
plt.show()