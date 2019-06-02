import pandas as pd

m_list = [1, 3, 5]

# 将列表转换为序列
pd_series = pd.Series(m_list)
pd_result = pd_series + 10
print(pd_result)

ls1 = [1, 3, 5]
series1 = pd.Series(ls1)
# x^2
temp = pow(series1, 2)
print(temp)

"""
序列的索引，成员关系，排重，排序，计数，抽样，统计运算
"""
print('****** 序列的索引，成员关系，排重，排序，计数，抽样，统计运算 ******')
import numpy as np

np.random.seed(1)
s1 = pd.Series(np.random.randint(size=5, low=1, high=10))
print(s1, '\n')

print('**** 取第一个元素 ****')
print(s1[0], '\n')
print('**** 取第2~3个元素 ****')
print(s1[1:3], '\n')
print('**** 依次取元素，步长为2 ****')
print(s1[::2], '\n')

print('倒数取元素(简洁并高速)：')
print(s1)
print(s1.iat[-3], '\n')
print(s1[-3:], '\n')

print('布尔索引：')
s2 = pd.Series(np.random.randint(size=5, low=1, high=100))
print(s2)
# 取出>=70的值
print(s2[s2 >= 70])
# 取出40到50之间的值
print('------')
print(s2[s2 >= 10][s2 <= 50])

# 一个向量的元素是否包含于另一个向量  np.in1d
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([10, 20, 3, 40])
print(np.in1d(arr1, arr2), '\n')

s1 = pd.Series(['A', 'B', 'C', 'D'])
s2 = pd.Series(['X', 'A', 'Y', 'D'])
print('s1 是否包含于 s2中')
print(s1.isin(s2), '\n')
print(np.in1d(s1, s2), '\n')

# 序列去重及水平统计
s = np.random.randint(size=1000, low=1, high=4)
print('序列去重及水平统计', '\n', s)
# 排重
print(pd.unique(s), '\n')
# 水平统计
print(pd.value_counts(s))

# 序列的排序
s = pd.Series(np.random.normal(size=4))
# 序列索引排序
print(s.sort_index(ascending=False), '\n')  # 降序排序
# 序列的值排序
print(s.sort_values())  # 按序列的实际值升序排序

# 抽样
print('***********  抽样 ********** ')
"""
s.sample(n=None, frac=None, replace=False, weights=None, random_state=None, axis=None)
n：指定抽取的样本量；
frac：指定抽取的样本比例；
replace：是否有放回抽样，默认无放回；
weights：指定样本抽中的概率，默认等概论抽样；
random_state：指定抽样的随机种子
"""

# 从1...100中随机抽取3个幸运儿
r_1 = pd.Series(range(1, 101))
print(r_1.sample(n=3, random_state=2), '\n')

# 从1...5中有放回的抽取3个值
r_2 = pd.Series(range(1, 6))
print(r_2.sample(n=3, replace=True, random_state=2), '\n')

# 从男、女性别中不等概率抽10个样本
r_3 = pd.Series(['男', '女'])
s_3 = r_3.sample(n=10, replace=True, weights=[0.2, 0.8], random_state=3)
print(s_3, '\n')

print('********  统计运算  *********')
np.random.seed(123)
s = pd.Series(np.random.randint(size=100, low=10, high=30))
print('原始值：', s, '\n')
s_des = s.describe()
print(s_des, '\n')

# 判断一个元素是否为缺失元素  isnull

s = pd.Series([1, 2, np.nan, 4, np.nan, 6])
print(s, '\n')
print(s.isnull)

print('**********  pandas 其他统计函数 ************')

others = \
    """
    s.min()  # 最小值
    s.quantile(q=[0,0.25,0.5,0.75,1]) # 分位数函数
    s.median()  # 中位数
    s.mode()  # 众数
    s.mean()  # 平均值
    s.mad()  # 平均绝对误差
    s.max  # 最大值
    s.sum()  # 和
    s.std()  # 标准差
    s.var()  # 方差
    s.skew()  # 偏度
    s.kurtosis()  # 峰度
    s.cumsum()  # 和的累计，返回序列
    s.cumprod()  # 乘积的累积，返回序列
    s.product()  # 序列元素乘积
    s.diff()  # 序列差异（微分），返回序列
    s.abs()  # 绝对值，返回序列
    s.pct_change()  # 百分比变化 ，返回序列
    s.corr(s2)  # 相关系数
    s.ptp()  # 极差  R中的range函数
    """
print(others)

p1 = np.random.randint(low=10, high=999, size=200)
min1 = p1.min()
max1 = p1.max()
print(min1)
print(max1)
cum1 = p1.cumsum()
print(cum1)
m1 = p1.mean()
print(m1)
print(p1.sum())