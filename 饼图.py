import numpy as np
import matplotlib.pyplot as plt

y = np.array([35, 25, 25, 15])

plt.pie(y,
        labels=['A', 'B', 'C', 'D'],  # 设置饼图标签
        colors=["#d5695d", "#5d8ca8", "#65a479", "#a564c9"],  # 设置饼图每块颜色
        explode=(0, 0.2, 0, 0),  # 第二部分突出显示，值越大，距离中心越远
        autopct='%.2f%%',  # 格式化输出百分比
        radius=8,
        counterclock=False,
        )
plt.xlim(-8, 8)
plt.ylim(-10, 10)
plt.title('Pie Test')  # 设置标题
plt.show()
