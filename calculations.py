# 统一即降级 (Unification-as-demotion)
# 报告数学推演复现代码

from scipy.constants import c  # 导入光速常量 (299792458 m/s)

def calculate_energy(mass):
    """
    根据爱因斯坦质能方程 E = mc^2 计算能量
    :param mass: 质量 (千克)
    :return: 能量 (焦耳)
    """
    if mass < 0:
        return "质量不能为负数"
    energy = mass * (c ** 2)
    return energy

def main():
    print("--- 统一即降级：质能方程复现 ---")
    try:
        # 获取用户输入的质量
        mass_input = float(input("请输入质量 (千克): "))
        
        # 计算结果
        result = calculate_energy(mass_input)
        
        # 输出结果
        print(f"对应的能量为: {result:.2e} 焦耳")
    except ValueError:
        print("请输入有效的数字！")

if __name__ == "__main__":
    main()
