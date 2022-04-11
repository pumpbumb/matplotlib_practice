"""
# 面向对象风格(o-o style)
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 400)
################################################################################################
# 创建一个 Figure 实例对象 fig1 ，标识为 1
fig1 = plt.figure(num=1, figsize=(10., 5.))
# 按住Ctrl，点击`figure`，查看其详细说明。
print(fig1.number)  # 上面的 1 就是 fig1 这个Figure对象的独一无二的标识；也可以是字符串，此时图像标签和窗口标题就是此字符串
fig1_ax1 = fig1.add_subplot(121)  # 创建一个 Axes 对象
fig1_ax1.plot(x, np.sin(x))
fig1_ax2 = fig1.add_subplot(122)  # 再创建一个 Axes 对象
fig1_ax2.plot(x, np.cos(x))
fig1.show()  # 显示fig1

"""
或者整合到一起一次性完成，适合于：(1) 知道自己要画多少个图  (2) 有共性[因为使用整合的方式，它们能共用很多性质]
"""
fig2, ax2 = plt.subplots(2, 2, num=2, figsize=(10., 5.))
print(fig2.number)
ax2[0, 0].plot(x, np.sin(x))  # 和`ndarray`索引一样
ax2[1, 1].plot(x, np.cos(x))
fig2.show()

################################################################################################
# 再创建一个 Figure 实例对象 fig3 ，标识为 3
fig3 = plt.figure(num=3, figsize=(8., 6.))
print(fig3.number)  # 上面的 3 就是 fig3 这个Figure对象的独一无二的标识
fig3_ax1 = fig3.add_subplot(221)  # 创建一个 Axes 对象
fig3_ax1.plot(x, np.exp(x), 'r--')
fig3_ax2 = fig3.add_subplot(224)  # 再创建一个 Axes 对象
fig3_ax2.plot(x, x ** 2, 'g')
fig3.show()  # 显示fig2

"""
或者整合到一起一次性完成，适合于：(1) 知道自己要画多少个图  (2) 有共性[因为使用整合的方式，它们能共用很多性质]
"""
fig4, ax4 = plt.subplots(3, 2, num=4, figsize=(8., 6.))
print(fig4.number)
ax4[0, 1].plot(x, np.exp(x), 'r--')
ax4[2, 0].plot(x, x ** 2, 'g')
fig4.show()
###############################################################################################
"""
# 官方注释：plt.subplots()  按住Ctrl, 再点击 subplots 查看
Typical idioms for handling the return value are::

            # using the variable ax for single a Axes
            fig, ax = plt.subplots()

            # using the variable axs for multiple Axes（我觉得第二种最好用，无非是ndarray索引）
            fig, axs = plt.subplots(2, 2)

            # using tuple unpacking for multiple Axes
            fig, (ax1, ax2) = plt.subplots(1, 2)  
            fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
            # 返回的是2D array, 所以写成 ((ax1, ax2), (ax3, ax4))
"""
#############################################################################################
"""
Examples
    --------
    ::

        # First create some toy data:
        x = np.linspace(0, 2*np.pi, 400)
        y = np.sin(x**2)

        # Create just a figure and only one subplot
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_title('Simple plot')

        # Create two subplots and unpack the output array immediately
        f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
        ax1.plot(x, y)
        ax1.set_title('Sharing Y axis')
        ax2.scatter(x, y)

        # Create four polar axes and access them through the returned array
        fig, axs = plt.subplots(2, 2, subplot_kw=dict(projection="polar"))
        axs[0, 0].plot(x, y)
        axs[1, 1].scatter(x, y)

        # Share a X axis with each column of subplots
        plt.subplots(2, 2, sharex='col')

        # Share a Y axis with each row of subplots
        plt.subplots(2, 2, sharey='row')

        # Share both X and Y axes with all subplots
        plt.subplots(2, 2, sharex='all', sharey='all')

        # Note that this is the same as
        plt.subplots(2, 2, sharex=True, sharey=True)

        # Create figure number 10 with a single subplot
        # and clears it if it already exists.
        fig, ax = plt.subplots(num=10, clear=True)
"""
