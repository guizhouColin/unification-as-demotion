# 狭义相对论：长度收缩效应可视化
import numpy as np
import matplotlib.pyplot as plt

c = 1 # 设光速为1

def length_contraction(v, l0):
    """根据洛伦兹因子计算收缩后的长度"""
    gamma = 1 / np.sqrt(1 - v**2 / c**2)
    return l0 / gamma

v = np.linspace(0, 0.99 * c, 100) # 速度从0到0.99倍光速
l0 = 1 # 飞船固有长度
l = length_contraction(v, l0)

plt.plot(v / c, l, color='blue')
plt.xlabel('速度 (v/c)')
plt.ylabel('收缩后的长度 (L)')
plt.title('狭义相对论：长度收缩效应')
plt.grid(True)
plt.show()
