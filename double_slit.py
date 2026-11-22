# 量子力学基础：双缝干涉实验模拟
import numpy as np
import matplotlib.pyplot as plt

def double_slit_interference(d, wavelength, L, x):
    """
    计算双缝干涉的光强分布
    :param d: 双缝间距
    :param wavelength: 光波长
    :param L: 屏幕到缝隙的距离
    :param x: 屏幕上的位置数组
    :return: 光强分布数组
    """
    # 计算相位差导致的光强分布 (I = I0 * cos^2(π*d*x / (wavelength*L)))
    phase = np.pi * d * x / (wavelength * L)
    intensity = np.cos(phase)**2
    return intensity

def main():
    print("--- 双缝干涉实验模拟 ---")
    
    # 模拟参数
    d = 0.0001       # 双缝间距 (米)
    wavelength = 500e-9 # 光波长 (米，500nm绿光)
    L = 1.0          # 屏幕距离 (米)
    
    # 屏幕位置范围
    x = np.linspace(-0.01, 0.01, 500) 
    
    # 计算光强
    intensity = double_slit_interference(d, wavelength, L, x)
    
    # 绘制干涉条纹
    plt.plot(x * 1000, intensity, color='green') # 转换为毫米显示
    plt.xlabel('屏幕位置 (mm)')
    plt.ylabel('相对光强')
    plt.title('双缝干涉条纹模拟')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
