import cv2
import numpy as np
import os

# 读取目标图像
target_img = cv2.imread("D:/waterbot/IMAGE.png")

# 读取图片数据集中的所有图像
images = []
for filename in os.listdir("D:/waterbot"):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        img = cv2.imread(os.path.join("D:/waterbot", filename))
        images.append(img)

# 创建SIFT对象
sift = cv2.SIFT_create()

# 提取目标图像的特征点和描述符
kp1, des1 = sift.detectAndCompute(target_img, None)

# 提取数据集中的所有图像的特征点和描述符
kps = []
dess = []
for img in images:
    kp, des = sift.detectAndCompute(img, None)
    kps.append(kp)
    dess.append(des)

# 使用FLANN算法计算特征点之间的距离
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks=50)   # or pass empty dictionary

flann = cv2.FlannBasedMatcher(index_params,search_params)

# 存储相似度结果
similarity_scores = []
for i, des2 in enumerate(dess):
    matches = flann.knnMatch(des1, des2, k=2)

    # 应用比率测试
    good = []
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            good.append(m)

    # 计算相似度分数
    similarity_score = len(good) / len(des1)
    similarity_scores.append(similarity_score)

# 找到最相似的两张图片
top_indices = np.argsort(similarity_scores)[-2:]  # 找到两个最大值的索引
top_images = [images[i] for i in top_indices]

# 展示三张图片和SIFT特征点
cv2.imshow("Target Image", target_img)
cv2.drawKeypoints(target_img, kp1, target_img, color=(0, 0, 255), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow("Target Image with SIFT", target_img)

for i, img in enumerate(top_images):
    cv2.imshow(f"Image {i+1}", img)
    cv2.drawKeypoints(img, kps[top_indices[i]], img, color=(0, 0, 255), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imshow(f"Image {i+1} with SIFT", img)

cv2.waitKey(0)
cv2.destroyAllWindows()