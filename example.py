import numpy as np
import matplotlib
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, num=20)  # 只生成20个点
y = np.sin(x)

# 有时候，我们不希望改变全局的风格，只是想暂时改变一下风格，则可以使用 context 将风格改变限制在某一个代码块内：
with plt.style.context('dark_background'):
    plt.plot(x, y, 'w-+')  # - 表示用直线连接
    plt.show()

plt.plot(x, y, 'r-o')
plt.show()

print(matplotlib.get_configdir())
