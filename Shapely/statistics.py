# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd
# from scipy.interpolate import make_interp_spline
#
# plt.figure(figsize=(16, 10), dpi=80)
#
# categories = ['celebrity', 'film&TV', 'artwork', 'models', 'design', 'game']
# # factors = ['base model', 'lora', 'control', 'ket prompt']
# # base_model = [3164, 3210, 3031, 1711, 1962, 3383]
# # lora = [2959, 2893, 2167, 1711, 1158, 2764]
# # controlnet = [1526, 1037, 1196, 576, 352, 1338]
# # key_prompt = [3079, 2574, 2386, 1077, 1286, 1996]
#
# # data = {
# #     [3164, 2959, 1526, 3079],
# #     [3210, 2893, 1037, 2574],
# #     [3031, 2167, 1196, 2386],
# #     [3383, 2764, 1338, 1996],
# #     [1962, 1158, 352, 1286],
# #     [1711, 1711, 576, 1077]
# # }
#
# data = {
#     'base_model': (3164, 3210, 3031, 3383, 1962, 1711),
#     'lora': (2959, 2893, 2167, 2764, 1158, 1711),
#     'controlnet': (1526, 1037, 1196, 1338, 352, 576),
#     'key_prompt': (3079, 2574, 2386, 1996, 1286, 1077)
# }
#
# data2 = {
#     'base_model': (0, 0, 0, 0, 0, 0),
#     'lora': (205, 317, 864, 619, 804, 0),
#     'controlnet': (1638, 2173, 1835, 2045, 1610, 1135),
#     'key_prompt': (85, 636, 645, 1387, 676, 634)
# }
#
# # llist = [3164, 3210, 3031, 3383, 1962, 1711]
# # for factor, numbs in data.items():
# #     c = [llist[i] - numbs[i] for i in range(0, len(llist))]
# #     print(c)
# #
#
# colors = [
#     ['#1F77B4', '#1F77B4'],
#     ['#FF7F0E', '#FFCA33'],
#     ['#2CA02C', '#7BA069'],
#     ['#D62728', '#D66C7C']
# ]
# x = np.arange(6)
# width = 0.20
# n = 0
# for key1, key2 in zip(data.items(), data2.items()):
#     offset = width * n
#     plt.bar(x + offset, key1[1], width, label=key1[0], color=colors[n][0])
#     plt.bar(x + offset, key2[1], width, color=colors[n][1], bottom=key1[1])
#     n += 1
#
#
# plt.legend(loc='best', fontsize=23)
# plt.xticks(x + 0.3, categories)
#
# plt.title("AAA", fontdict={'size': 50})
# plt.xlabel('Contribution Value', fontdict={'size': 36})
# plt.yticks(range(0, 4000, 500))
#
# plt.tick_params(labelsize=30)
# plt.rcParams['font.sans-serif'] = 'Sitka'
# plt.savefig("../result/factors_bar.svg")
# plt.show()
#
#
# # plt.bar(categories, base_model, width=0.25, color='#2E74B0', label='base model')
# # plt.bar(categories, lora, width=0.25, color='#FCAC68', label='lora')
# # plt.bar(categories, controlnet, width=0.25, color='#B4FF5E', label='controlnet')
# # plt.bar(categories, key_prompt, width=0.25, color='#D43B11', label='key prompt')
# #
# # plt.legend(loc='best', fontsize=23)
# #
# # plt.grid(True, axis='y', ls='--')
# #
# #
# # plt.title("Contribution of factors in LOO", fontdict={'size': 50})
# # plt.xlabel('Contribution Value', fontdict={'size': 36})
# #
# # plt.tick_params(labelsize=30)
# # plt.rcParams['font.sans-serif'] = 'Sitka'
# # plt.savefig("../result/factors_bar.svg")
# # plt.show()
#
#
# # import numpy as np
# # years = np.arange(2018, 2023)
# # areas = ("PRC", "USA", "EU")
# # GDPS = {
# #     'PRC': (13.89, 14.28, 14.69, 17.82, 17.96),
# #     'USA': (20.53, 21.38, 21.06, 23.32, 25.46),
# #     'EU': (15.98, 15.69, 15.37, 17.19, 16.64),
# # }
# #
# # import matplotlib.pyplot as plt
# #
# # x = np.arange(len(years))
# #
# # print(x, type(x))
# # width = 0.25
# #
# # n = 0
# # for area, gdp in GDPS.items():
# #     offset = width * n
# #     rects = plt.bar(x + offset, gdp, width, label=area)
# #     plt.bar_label(rects, padding=3)
# #     n += 1
# #
# # plt.ylabel('GDP/$trilion')
# # plt.ylim(10, 28)
# # plt.xticks(x + width, years.astype(str))
# # plt.legend(loc='upper left')
# #
# # plt.show()


