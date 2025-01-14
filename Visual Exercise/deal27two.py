import cv2
import numpy as np

def gaussian_kernel(ksize, sigma):
    """
    生成高斯核函数

    Args:
        ksize: 核大小
        sigma: 标准差

    Returns:
        高斯核矩阵
    """

    if ksize % 2 == 0:
        raise ValueError("核大小必须为奇数")

    center = ksize // 2
    x, y = np.mgrid[-center:center+1, -center:center+1]
    kernel = np.exp(-(x**2 + y**2) / (2 * sigma**2))
    return kernel / np.sum(kernel)

def main():
    """
    主函数
    """

    # 设置参数
    ksize = 3
    sigma = 0.8

    # 生成高斯核
    kernel = gaussian_kernel(ksize, sigma)

    # 加载图片
    img = cv2.imread("D:\\waterbot\\two.png")

    # 使用高斯核卷积图像
    dst = cv2.filter2D(img, -1, kernel)

    # 保存结果图像
    cv2.imwrite("D:\\waterbot\\two_gaussian.png", dst)

if __name__ == "__main__":
    main()