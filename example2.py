import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array([2, 6, 9])
ypoints = np.array([4, 66, 100])

plt.subplot(121)
plt.plot(xpoints, ypoints)  # 默认会用直线相连

plt.subplot(122)
plt.plot(xpoints, ypoints, 'r*')
plt.show()
