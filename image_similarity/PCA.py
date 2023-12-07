import csv
from sklearn.decomposition import PCA
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

SSIM_path = "../data/SSIM.csv"
FID_path = "../data/FID.csv"
STYLE_path = "../data/STYLE.csv"
# PART_path = "../data/PART.csv"

SSIM_data = pd.read_csv(SSIM_path)
FID_data = pd.read_csv(FID_path)
STYLE_data = pd.read_csv(STYLE_path)
# PART_data = pd.read_csv(PART_path)

FID_data = FID_data.apply(lambda x: (x - np.min(x)) / (np.max(x) - np.min(x)))
SSIM_data = SSIM_data.apply(lambda x: (x - np.min(x)) / (np.max(x) - np.min(x)))
STYLE_data = STYLE_data.apply(lambda x: (x - np.min(x)) / (np.max(x) - np.min(x)))

alliance = []
for j in range(1, 15):
    col_name = 'images' + str(j)
    alliance_data = []
    for i in range(0, 100):
        row = [SSIM_data[col_name][i], FID_data[col_name][i], STYLE_data[col_name][i]]  # , STYLE_data[col_name][i], PART_data[col_name][i]
        alliance_data.append(row)

    # list转np.array
    np_data = np.array(alliance_data)
    plt.scatter(np_data[:, 0], np_data[:, 1], np_data[:, 2])
    plt.title('Data before PCA')
    plt.show()

    # PCA降维
    pca = PCA(n_components=1)
    pca.fit(alliance_data)
    pca_data = pca.transform(alliance_data)

    plt.scatter(pca_data, pca_data)
    plt.title('Data after PCA')
    plt.show()

    mean = np.mean(pca_data)
    print(mean)


