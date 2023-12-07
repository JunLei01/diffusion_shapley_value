# diffusion_shapley_value
**Research on copyright attribution issues in image generation at the model level**

### Overview

![](https://github.com/JunLei01/diffusion_shapley_value/blob/main/material/overview.png)
## Abstract

Web-based AI image generation has become an innovative art form that can generate novel artworks with the rapid development of the diffusion model. However, this new technique brings potential copyright infringement risks as it may incorporate the existing artworks without the owners' consent. Copyright infringement quantification is the primary and challenging step towards AI-generated image copyright traceability. Previous work only focused on data attribution from the training data perspective, which is unsuitable for tracing and quantifying copyright infringement in practice because of the following reasons: (1) the training datasets are not always available in public; (2) the model provider is the responsible party, not the image. Motivated by this, in this paper, we propose **CopyScope**, a new framework to quantify the infringement of AI-generated images from the model level. We first rigorously identify pivotal components within the AI image generation pipeline. Then, we propose to take advantage of Fréchet Inception Distance (FID) to effectively capture the image similarity that fits human perception naturally. We further propose the FID-based Shapley algorithm to evaluate the infringement contribution among models. Extensive experiments demonstrate that our work not only reveals the intricacies of infringement quantification but also effectively depicts the infringing models quantitatively, thus promoting accountability in AI image-generation tasks.

## Quantitative results under different Quantitative metrics

![Figure 1](https://github.com/JunLei01/diffusion_shapley_value/blob/main/material/figure1.png)

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

## Pixel Difference Experiment

![Figure 2](https://github.com/JunLei01/diffusion_shapley_value/blob/main/material/pixel%20image.png)

## FID-Shapley

'''math
\textbf{FID} = {\parallel \mu_r - \mu_g \parallel}_2^2 + Tr(\Sigma_r + \Sigma_g - 2(\Sigma_r \Sigma_g)^{1/2}). \\
v_{SV}(z_i) \propto \frac{1}{N}\sum_{\mathcal{L} \subseteq \mathcal{M} \setminus {z_i}} [U(\mathcal{L} \cup {z_i})-U(\mathcal{L})] \frac{| \mathcal{L} |!(N-1-|\mathcal{L}|)!}{(N-1)!}.
'''

## Contribution of the models

![](https://github.com/JunLei01/diffusion_shapley_value/blob/main/material/result1.png)

## Ablation experiment

![](https://github.com/JunLei01/diffusion_shapley_value/blob/main/material/figure7.png)
