# import numpy as np
# import matplotlib.pyplot as plt
#
# plt.figure(figsize=(18, 15), dpi=80)
# image_batches = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Davinci = [169.01598553125626, 181.25897189289753, 168.50521709005432, 170.1348942478634, 159.67737149731096, 165.68861526779497, 181.2184621829933, 179.05343385371515, 171.1662634321177, 162.6626878261081]
# NoDavinciReg = [ 214.25567195610253, 249.64069685125833, 210.36026122499308, 265.77966539291634, 257.02075552778035, 278.23035974552835, 244.03791966736256,  220.52453647798976,  203.89147838945857, 229.72143629813053]
# NoDavinciRan = [ 244.9813587039938,  220.47649557948725, 217.25601094022213, 230.45152146834914,  235.9680601196277,  240.37819617249338, 234.25943733103108,  227.831731416932, 234.39453525274362, 219.83344247175646]
#
# aveDavinci = np.mean(Davinci)
# aveNoDavinciReg = np.mean(NoDavinciReg)
# aveNoDavinciRan = np.mean(NoDavinciRan)
#
#
# plt.plot(image_batches, Davinci, c='red', linewidth=4.0, label="Depth")
# plt.plot(image_batches, NoDavinciReg, c='green', linewidth=4.0, label="No Depth(regularize seed)")
# plt.plot(image_batches, NoDavinciRan, c='blue', linewidth=4.0, label="No Depth(random seed)")
# plt.scatter(image_batches, Davinci, c='red')
# plt.scatter(image_batches, NoDavinciReg, c='green')
# plt.scatter(image_batches, NoDavinciRan, c='blue')
# plt.legend(loc='best', fontsize=30)
# plt.yticks(range(100, 400, 20))
# plt.tick_params(labelsize=30)
#
# plt.axhline(aveDavinci, color='red', linewidth=1.5, linestyle='dashdot')
# plt.axhline(aveNoDavinciReg, color='green', linewidth=1.5, linestyle='dashdot')
# plt.axhline(aveNoDavinciRan, color='blue', linewidth=1.5, linestyle='dashdot')
#
# plt.xlabel("Image Batches", fontdict={'size': 36})
# plt.ylabel("FID value", fontdict={'size': 36})
# plt.title("Contribution verification of factor 'Depth'", fontdict={'size': 50})
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
#
# plt.figure(figsize=(18, 15), dpi=80)
# image_batches = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Davinci = [187.5538700160699, 183.7186366778351, 196.2072545420947, 186.44723375554682, 171.43666330607527, 174.74947476212557,  171.6570877829301,  166.76699628335413, 161.02321845319304, 179.51886452524457]
# NoDavinciReg = [229.85459801857797, 231.99886222669588, 206.65031442598163, 235.81860127614465, 283.29999270148284, 246.73735994996255, 232.65376944551178, 220.92373058366033, 205.0088016559555, 305.2560167994768]
# NoDavinciRan = [216.419767020026, 308.9437523988633, 237.7119532878188, 228.34670834784072, 262.3305779109504, 288.00179348519487, 287.70547927093514, 226.96301552505673, 271.4618412957291, 294.4729310352721]
#
# aveDavinci = np.mean(Davinci)
# aveNoDavinciReg = np.mean(NoDavinciReg)
# aveNoDavinciRan = np.mean(NoDavinciRan)
#
# plt.plot(image_batches, Davinci, c='red', linewidth=4.0, label="Davinci")
# plt.plot(image_batches, NoDavinciReg, c='green', linewidth=4.0, label="No Davinci(regularize seed)")
# plt.plot(image_batches, NoDavinciRan, c='blue', linewidth=4.0, label="No Davinci(random seed)")
#
# plt.scatter(image_batches, Davinci, c='red')
# plt.scatter(image_batches, NoDavinciReg, c='green')
# plt.scatter(image_batches, NoDavinciRan, c='blue')
# plt.legend(loc='best', fontsize=30)
# plt.yticks(range(100, 400, 20))
# plt.tick_params(labelsize=30)
#
# plt.axhline(aveDavinci, color='red', linewidth=1.5, linestyle='dashdot')
# plt.axhline(aveNoDavinciReg, color='green', linewidth=1.5, linestyle='dashdot')
# plt.axhline(aveNoDavinciRan, color='blue', linewidth=1.5, linestyle='dashdot')
#
# plt.xlabel("Image Batches", fontdict={'size': 36})
# plt.ylabel("FID value", fontdict={'size': 36})
# plt.title("Contribution verification of factor 'Davinci'", fontdict={'size': 50})
# plt.show()


''''''
# import numpy as np
# import matplotlib.pyplot as plt
#
# plt.figure(figsize=(18, 15), dpi=80)
# image_batches = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Davinci = [169.01598553125626, 181.25897189289753, 168.50521709005432, 170.1348942478634, 159.67737149731096, 165.68861526779497, 181.2184621829933, 179.05343385371515, 171.1662634321177, 162.6626878261081]
# NoDavinciReg = [ 214.25567195610253, 249.64069685125833, 210.36026122499308, 265.77966539291634, 257.02075552778035, 278.23035974552835, 244.03791966736256,  220.52453647798976,  203.89147838945857, 229.72143629813053]
# NoDavinciRan = [ 244.9813587039938,  220.47649557948725, 217.25601094022213, 230.45152146834914,  235.9680601196277,  240.37819617249338, 234.25943733103108,  227.831731416932, 234.39453525274362, 219.83344247175646]
#
# aveDavinci = np.mean(Davinci)
# aveNoDavinciReg = np.mean(NoDavinciReg)
# aveNoDavinciRan = np.mean(NoDavinciRan)
#
# plt.plot(image_batches, Davinci, c='red', label="SDMv10")
# plt.plot(image_batches, NoDavinciReg, c='green', label="No SDMv10(regularize seed)")
# plt.plot(image_batches, NoDavinciRan, c='blue', label="No SDMv10(random seed)")
#
# plt.scatter(image_batches, Davinci, c='red')
# plt.scatter(image_batches, NoDavinciReg, c='green')
# plt.scatter(image_batches, NoDavinciRan, c='blue')
# plt.legend(loc='best', fontsize=30)
# plt.yticks(range(100, 400, 20))
# plt.tick_params(labelsize=30)
#
# plt.axhline(aveDavinci, color='red', linewidth=1, linestyle='dashdot')
# plt.axhline(aveNoDavinciReg, color='green', linewidth=0.5, linestyle='dashdot')
# plt.axhline(aveNoDavinciRan, color='blue', linewidth=0.5, linestyle='dashdot')
#
# plt.xlabel("Image batches", fontdict={'size': 36})
# plt.ylabel("FID value", fontdict={'size': 36})
# plt.title("Contribution verification of factor 'Depth'", fontdict={'size': 50})
# plt.show()


import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

plt.figure(figsize=(18, 15), dpi=80)
image_batches = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
Davinci = [158.6768608, 170.4332577, 167.1814681, 157.3921996, 169.7110656, 182.8658247, 168.2195382,
           151.7944164, 174.0513618, 187.995118, 179.6757423, 184.7799313, 179.4774833, 171.2635547, 181.1875554,
           170.7764741, 159.5571663, 170.7716627, 168.9927337, 184.4300518]
NoDavinciReg = [254.9330232, 335.3446439, 346.584785, 312.0677771, 343.5653063, 269.4990808, 299.1897883, 337.5756053,
                311.4793628, 335.182784, 339.9801233, 322.130186, 306.6469758, 290.3636918, 346.2151365, 280.4301054,
                312.1898589, 331.8428296, 256.182582, 281.8249599]
NoDavinciRan = [293.0513986, 289.8733377, 334.4806465, 330.5863844, 321.5609779, 294.7746829, 348.1533868, 355.5481163,
                341.6540727, 357.406409, 265.887422, 269.4990808, 304.5699039, 293.4001832, 291.2653695, 291.8294906,
                319.4957558, 324.8527482, 268.1709583, 291.4489273]


def smooth_xy(lx, ly):
    """数据平滑处理

    :param lx: x轴数据，数组
    :param ly: y轴数据，数组
    :return: 平滑后的x、y轴数据，数组 [slx, sly]
    """
    x = np.array(lx)
    y = np.array(ly)
    x_smooth = np.linspace(x.min(), x.max(), 300)
    y_smooth = make_interp_spline(x, y)(x_smooth)
    return [x_smooth, y_smooth]


aveDavinci = np.mean(Davinci)
aveNoDavinciReg = np.mean(NoDavinciReg)
aveNoDavinciRan = np.mean(NoDavinciRan)

stdDavinci = np.std(Davinci)
stdNoDavinciReg = np.std(NoDavinciReg)
stdNoDavinciRan = np.std(NoDavinciRan)

plt.plot(image_batches, Davinci, c='#D76364', linewidth=4.0, marker='o', markersize='20', label="All Models Alliances")
plt.plot(image_batches, NoDavinciReg, c='#54B345', linewidth=4.0, marker='v', markersize='20',
         label="NoDavinci Alliances(reg seed)")
plt.plot(image_batches, NoDavinciRan, c='#2E74B0', linewidth=4.0, marker='s', markersize='20',
         label="NoDavinci Alliances(ran seed)")
plt.fill_between(image_batches, Davinci - stdDavinci, Davinci + stdDavinci, facecolor='#EF7A6D', alpha=0.3)
plt.fill_between(image_batches, NoDavinciReg - stdNoDavinciReg, NoDavinciReg + stdNoDavinciReg, facecolor='#32B897',
                 alpha=0.3)
plt.fill_between(image_batches, NoDavinciRan - stdNoDavinciRan, NoDavinciRan + stdNoDavinciRan, facecolor='#AAD2F9',
                 alpha=0.3)

plt.scatter(image_batches, Davinci, c='#FCAC68')
plt.scatter(image_batches, NoDavinciReg, c='#26A03E')
plt.scatter(image_batches, NoDavinciRan, c='#2E74B0')
plt.legend(loc='best', fontsize=34)
plt.yticks(range(120, 380, 40))
# plt.sticks((range(-1, 21, 2)))
plt.tick_params(labelsize=34)

plt.xlabel("Image Batches", fontdict={'size': 36})
plt.ylabel("FID value", fontdict={'size': 36})
plt.title("Contribution of the model 'Davinci'", fontdict={'size': 50})
plt.rcParams['font.sans-serif'] = 'Sitka'
plt.savefig('../result/second_plot/Davinci.svg')
plt.show()
