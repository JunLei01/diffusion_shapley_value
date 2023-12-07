# import matplotlib.pyplot as plt
# # from matplotlib import font_manager
# #
# # for font in font_manager.fontManager.ttflist:
# #     print(font.name, '-', font.fname)
#
# plt.figure(figsize=(20,5), dpi=80)
# # 数据
# categories = ['SDv1-5', 'SDMv10', 'Depth', 'Davinci', 'MonaLisa', 'Leonardo']
# positive_values = [0, 0.4546, 0.0056, 0, 0, 0.1285]
# negative_values = [0, 0, 0, -0.3308, -0.0803, 0]
#
# # 绘制图形
# fig, ax = plt.subplots()
# # 绘制正值条形图
# ax.barh(categories, positive_values, color='#2E74B0', label='positive_contribution')
#
# # 绘制负值条形图
# ax.barh(categories, negative_values, color='#FCAC68', label='negative_contribution')
#
# # 调整y轴范围
# # ax.set_ylim(min(-1), max(1))
#
# # 添加网格线
# ax.grid(True, axis='y', linestyle='--')
# ax.axvline(0.0, color='black', linewidth=0.5)
# # 添加标题和标签
# ax.set_title('Contribution of Each Factor', fontdict={'size': 17})
# ax.set_xlabel('Contribution Value', fontdict={'size': 12})
# ax.set_ylabel('Factors', loc='top')
# plt.tick_params(labelsize=10)
# plt.rcParams['font.sans-serif'] = 'Sitka'
#
# # 显示图形
# plt.show()

# LOO Data
# positive_values = [0.4546, 0.0056, 0, 0, 0.1285, 0]
# negative_values = [0, 0, -0.3308, -0.0803, 0, 0]
# Shapley
# positive_values = [0, 0.2823, 0.4847, 0.1173, 0.0806, 0]
# negative_values = [-0.0354, 0, 0, 0, 0, 0]



import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

plt.figure(figsize=(16, 10), dpi=96)

categories = ['SDMv10', 'Depth', 'Davinci', 'MonaLisa', 'Leonardo', 'SDv1-5']
positive_values = [0.4546, 0.0056, 0, 0, 0.1285, 0]
negative_values = [0, 0, -0.3308, -0.0803, 0, 0]

plt.barh(categories, positive_values, color='#2E74B0', label='Positive Contribution')
plt.barh(categories, negative_values, color='#FCAC68', label='Negative Contribution')
plt.legend(loc='best', fontsize=23)

plt.grid(True, axis='y', ls='--')
plt.axvline(0.0, color='black', linewidth='0.5')

plt.title("Contribution of the models in FID-LOO", fontdict={'size': 50})
plt.xlabel('Contribution Value', fontdict={'size': 36})
# plt.ylabel('Factors', fontdict={'size': 36})

plt.tick_params(labelsize=30)
plt.rcParams['font.sans-serif'] = 'Sitka'
plt.savefig("../result/LOO_bar.svg")
plt.show()