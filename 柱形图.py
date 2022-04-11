import matplotlib.pyplot as plt
import numpy as np

x = np.array(["monday", "tuesday", "saturday", "sunday"])
y = np.array([12, 22, 6, 18])

plt.subplot(211)
plt.bar(x, y, color=["#4CAF50", "red", "hotpink", "#556B2F"], width=0.1)  # 设置每个柱的颜色

plt.subplot(212)
plt.barh(x, y, color='#39aabb', height=0.5)
plt.show()
