import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# 导入数据集
fmri = sns.load_dataset("fmri")
print(list(fmri))  # 获取所有列名
print(fmri.nunique())  # 获取每一列中有多少个不同的数据
print(fmri.shape)  # 获取数据集大小
print(fmri.head(5))  # 打印前5行
fmri_time = fmri.loc[:, 'timepoint']  # 获取 timepoint 列的所有数据
print(fmri_time)

# 绘图
sns.relplot(x="timepoint", y="signal", data=fmri)
plt.show()
sns.relplot(x="timepoint", y="signal", kind="line", data=fmri)
plt.show()
sns.relplot(x="timepoint", y="signal", ci=None, kind="line", data=fmri)
plt.show()
sns.relplot(x="timepoint", y="signal", kind="line", ci="sd", data=fmri)
plt.show()
sns.relplot(x="timepoint", y="signal", estimator=None, kind="line", data=fmri)
plt.show()