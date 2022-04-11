"""
# pyplot风格
"""
import matplotlib.pyplot as plt

# 创建多个画布
plt.figure(1, figsize=(10., 10.))  # the first figure
plt.subplot(211)  # the first subplot in the first figure
plt.plot([1, 2, 3])
plt.subplot(212)  # the second subplot in the first figure
plt.plot([4, 5, 6])

plt.figure(2, figsize=(10., 10.))  # a second figure
plt.plot([4, 5, 6])  # creates a subplot() by default

plt.figure(1)  # figure 1 current; subplot(212) still current
plt.subplot(211)  # make subplot(211) in figure1 current
plt.title('figure(1)')  # subplot 211 title

#########################################################################
plt.figure(2)  # 切换到figure(2)
plt.title('figure(2)')

#########################################################################
plt.show()  # 显示所有
