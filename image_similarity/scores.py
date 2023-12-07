import os
import csv

import pandas as pd

os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
from pathlib import Path
from moudles import calculate

calc = calculate()
# origin_img = "D:/MyGraduate/code/diffusion_shapely_value/images/origin_imgs/mona_lisa.png"
# generate_imgs = "D:/MyGraduate/code/diffusion_shapely_value/images/generate_imgs/first_images/20.png"
# calc.image1 = origin_img
# calc.image2 = generate_imgs
#
# data = [calc.calculate_image_cosin(),
#         calc.calculate_image_hist(),
#         calc.calculate_image_dHash(),
#         calc.calculate_image_ssim(),
#         calc.calculate_image_RGB_ssim()]
# print(data)

root_path = "D:/MyGraduate/paper/WWW/diffusion_shapely_value/data/images15"
origin_img = "D:/MyGraduate/paper/WWW/diffusion_shapely_value/images/origin_imgs/mona_lisa.png"
calc.image1 = origin_img

# 读取文件夹下所有的文件夹

for gen_image in os.listdir(root_path):
    # 判断gen_image是否为空
    image_path = root_path + "/" + gen_image
    if not os.path.isdir(image_path):
        continue
    # 读取gen_image中的文件
    for image in os.listdir(image_path):
        calc.image2 = image_path + "/" + image
        data = calc.calculate_image_RGB_ssim()
        print(data)
        # data_rows.append(data)
        # print(data_rows)

# new_csv = "D:/MyGraduate/code/diffusion_shapely_value/data/LOO_compositions_orsize.csv"
# f = open(new_csv, 'w', encoding='utf-8', newline='')
# head = ["no.", "element", "SSIM", "Cosin", "Histogram", "DHash", "RGBSSIM"]
# writer = csv.writer(f)
# writer.writerow(head)
#
# with open("D:/MyGraduate/code/diffusion_shapely_value/data/compositions.csv", 'r', encoding='utf-8') as fp:
#     reader = csv.DictReader(fp)
#     data_rows = []
#
#
#     def find_row(name):
#         for row in reader:
#             if row['no.'] == name.split('.')[0]:
#                 fp.seek(0)
#                 return row['element']
#             else:
#                 continue
#         fp.seek(0)
#         return None
#
#
#     for gen_image in Path(generate_imgs).iterdir():
#         calc.image2 = str(gen_image)
#         name = str(Path(gen_image).name)
#         element = find_row(name)
#         if element is None:
#             continue
#
#         data = [name.split('.')[0],
#                 # element,
#                 calc.calculate_image_cosin(),
#                 calc.calculate_image_hist(),
#                 calc.calculate_image_dHash(),
#                 calc.calculate_image_ssim(),
#                 calc.calculate_image_RGB_ssim()]
#         print(data)
#         data_rows.append(data)
#         # print(data_rows)
#
#     # writer.writerows(data_rows)
#     # fp.close()
# f.close()
