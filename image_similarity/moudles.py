import numpy as np
import math
import cv2
from dHash import DHash
import torch
import pytorch_ssim
from torch.autograd import Variable
from PIL import Image
from skimage.metrics import structural_similarity as SSIM


class calculate(DHash):
    def __init__(self):
        self.image1 = None
        self.image2 = None

    def calculate_image_cosin(self):

        def get_thum(image, size=(64, 64), greyscale=False):
            image = Image.open(image)
            image = image.resize(size, Image.LANCZOS)
            if greyscale:
                # 将图片转换为L模式，其为灰度图，其每个像素用8个bit表示
                image = image.convert('L')
            return image

        img1 = get_thum(self.image1)
        img2 = get_thum(self.image2)
        images = [img1, img2]
        vectors = []
        norms = []
        for image in images:
            vector = []
            for pixel_tuple in image.getdata():
                vector.append(np.average(pixel_tuple))
            vectors.append(vector)
            # linalg=linear（线性）+algebra（代数），norm则表示范数
            # 求图片的范数？？
            norms.append(np.linalg.norm(vector, 2))
        a, b = vectors
        a_norm, b_norm = norms
        # dot返回的是点积，对二维数组（矩阵）进行计算
        cosin_value = np.dot(a / a_norm, b / b_norm)
        return cosin_value

    '''
    SSIM formula：
    \hbox{SSIM}(x,y) = \frac{(2\mu_x\mu_y + c_1)(2\sigma_{xy} + c_2)}{(\mu_x^2 + \mu_y^2 + c_1)(\sigma_x^2 + \sigma_y^2 + c_2)}
    '''

    def calculate_image_ssim(self):
        img1 = cv2.imread(self.image1)
        img2 = cv2.imread(self.image2)
        img2 = np.resize(img2, (img1.shape[0], img1.shape[1], img1.shape[2]))

        ssim_value = SSIM(img1, img2, multichannel=True, channel_axis=2)
        return ssim_value

    def calculate_image_hist(self, hist_size=256):
        img1 = cv2.imread(self.image1)
        img2 = cv2.imread(self.image2)

        def normalize(data):
            return data / np.sum(data)
        
        imghistB1 = cv2.calcHist([img1], [0], None, [hist_size], [0, 256])
        imghistG1 = cv2.calcHist([img1], [1], None, [hist_size], [0, 256])
        imghistR1 = cv2.calcHist([img1], [2], None, [hist_size], [0, 256])

        imghistB2 = cv2.calcHist([img2], [0], None, [hist_size], [0, 256])
        imghistG2 = cv2.calcHist([img2], [1], None, [hist_size], [0, 256])
        imghistR2 = cv2.calcHist([img2], [2], None, [hist_size], [0, 256])

        distanceB = cv2.compareHist(normalize(imghistB1), normalize(imghistB2), cv2.HISTCMP_CORREL)
        distanceG = cv2.compareHist(normalize(imghistG1), normalize(imghistG2), cv2.HISTCMP_CORREL)
        distanceR = cv2.compareHist(normalize(imghistR1), normalize(imghistR2), cv2.HISTCMP_CORREL)
        hist_value = np.mean([distanceB, distanceG, distanceR])
        return hist_value

    def calculate_image_dHash(self):
        image1 = Image.open(self.image1)
        image2 = Image.open(self.image2)

        dhash1 = calculate.calculate_hash(image1)
        dhash2 = calculate.calculate_hash(image2)
        print(dhash2, dhash1, len(dhash1), len(dhash2))

        hamming_dis = calculate.hamming_distance(dhash1, dhash2)
        similarity = 1 - hamming_dis / 64

        return similarity

    def calculate_image_RGB_ssim(self):
        img1 = cv2.imread(self.image1)
        img2 = cv2.imread(self.image2)
        u_true = np.mean(img1)
        u_pred = np.mean(img2)
        var_true = np.var(img1)
        var_pred = np.var(img2)
        std_true = np.sqrt(var_true)
        std_pred = np.sqrt(var_pred)
        c1 = np.square(0.01 * 7)
        c2 = np.square(0.03 * 7)
        ssim = (2 * u_true * u_pred + c1) * (2 * std_pred * std_true + c2)
        denom = (u_true ** 2 + u_pred ** 2 + c1) * (var_pred + var_true + c2)
        return ssim / denom
