# Multi-Dimensional Fusion Experiment

The specific experimental plan is as follows: We expanded two additional dimensions of indicators, **STYLE Similarity** and **PART Similarity**, based on the existing indicators. We also comprehensively considered the characteristics of different images, such as architectural images focusing more on structure, artistic images focusing more on color style, and portraits focusing more on the subjects themselves. Therefore, we have assigned three additional attribute dimensions **[SSIM, STYLE, PART]** to each image to describe the structural, stylistic, and subject features.

First, the structural attribute corresponding to SSIM remains unchanged from **Section 2.2** of our paper, and the SSIM value of each image is calculated. The STYLE attribute corresponds to the style property. We constructed a style extractor - VGG[1], to extract the style matrix of each image (the matrix dimension in this experiment is 3×736×512) and then calculated the cosine similarity of the style matrix and normalized it to obtain the style attribute value of the image. 

PART corresponds to the subject attribute. We use an image segmenter to identify and cut the central part of the image, extract features (we also keep the feature matrix as 3×736×512), then calculate the correlation and obtain the correlation score[2]. Then, we construct the image's attribute matrix **[SSIM, STYLE, PART]** and use the **PCA** algorithm to reduce the dimension of the image's attributes. Finally, we use the new fusion attributes to calculate the Shapley value and determine the contribution of each model. 

Distribution of data in the fused dimension indicator before and after dimensionality reduction using PCA method

<img src="https://github.com/JunLei01/diffusion_shapley_value/blob/main/material/BPCA.png" style="zoom:50%;" /><img src="https://github.com/JunLei01/diffusion_shapley_value/blob/main/material/APCA.png" style="zoom:50%;" />

Distribution of Fusion scores across different alliances

![](https://github.com/JunLei01/diffusion_shapley_value/blob/main/material/chart.png)



Quantitative results under different Quantitative metrics.(Add fusion metrics) 

| Figure No.  | Alliances                              | Cosine     | Hist       | DHash  | SSIM       | RGB-SSIM   | FID        | Fusion     |
| ----------- | -------------------------------------- | ---------- | ---------- | ------ | ---------- | ---------- | ---------- | ---------- |
| Figure (1)  | SDv1-5                                 | 0.8802     | 0.1511     | 0.5468 | 0.2934     | 0.8424     | 310.18     | 0.0821     |
| Figure (2)  | SDv1-5+Depth                           | 0.8927     | 0.3518     | 0.5000 | 0.4541     | 0.9251     | 289.24     | 0.0879     |
| Figure (3)  | SDv1-5+Depth+Davinci                   | **0.9817** | 0.5582     | 0.7656 | 0.9281     | **0.9971** | 239.17     | 0.0920     |
| Figure (4)  | SDv1-5+Depth+Davinci+MonaLisa          | 0.9087     | 0.5789     | 0.7500 | **0.9684** | 0.9963     | 233.21     | 0.0477     |
| Figure (5)  | SDv1-5+Depth+Davinci+MonaLisa+Leonardo | 0.8279     | 0.5356     | 0.7656 | 0.7463     | 0.9689     | 220.40     | 0.1015     |
| Figure (6)  | SDv1-5+Davinci                         | 0.9184     | 0.3734     | 0.4843 | 0.5275     | 0.9200     | 265.01     | 0.1981     |
| Figure (7)  | SDv1-5+Davinci+MonaLisa                | 0.9328     | 0.4591     | 0.6562 | 0.7235     | 0.9420     | 241.18     | 0.0371     |
| Figure (8)  | SDv1-5+Davinci+MonaLisa+Leonardo       | 0.8876     | 0.4085     | 0.5937 | 0.6065     | 0.9458     | 275.92     | 0.1101     |
| Figure (9)  | SDv1-5+MonaLisa                        | 0.8778     | 0.4417     | 0.3593 | 0.1982     | 0.8251     | 336.24     | 0.0226     |
| Figure (10) | SDv1-5+Leonardo                        | 0.8705     | 0.0964     | 0.6718 | 0.2673     | 0.9148     | 307.06     | 0.2419     |
| Figure (11) | SDMv10                                 | 0.8759     | 0.0372     | 0.7031 | 0.2568     | 0.8837     | 320.48     | 0.1798     |
| Figure (12) | SDMv10+Depth+Davinci                   | 0.8898     | 0.5227     | 0.7343 | 0.6214     | 0.9819     | 209.06     | 0.1688     |
| Figure (13) | SDMv10+Depth+Davinci+MonaLisa          | 0.8876     | **0.5891** | 0.7656 | 0.5766     | 0.9834     | 212.13     | **0.3774** |
| Figure (14) | SDMv10+Depth+Davinci+MonaLisa+Leonardo | 0.8605     | 0.4096     | 0.8593 | 0.4481     | 0.9733     | **184.69** | 0.0879     |

Shapley result:

|          | LOO-FID | FID-Shapley | Fusion-Shapely |
| :------- | :------ | :---------- | :------------- |
| Depth    | 0.0056  | 0.1983      | 0.0723         |
| Davinci  | -0.3308 | 0.4278      | 0.3297         |
| MonaLisa | -0.0803 | -0.2467     | 0.2685         |
| Leonardo | 0.1285  | 0.0296      | -0.1247        |
| SDMv10   | 0.4546  | -0.0975     | 0.2045         |

## Contribution of the models

![](https://github.com/JunLei01/diffusion_shapley_value/blob/main/material/result1.png)

## Ablation experiment

![](https://github.com/JunLei01/diffusion_shapley_value/blob/main/material/figure7.png)

Combining the results of the ablation experiment shown in Ablation experiment of the paper, we can easily see that the performance of **FID-Shapley** is closest to the results of the ablation experiment. 

