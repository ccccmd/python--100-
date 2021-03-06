# -*- coding:utf-8 -*-
# 画图，学用circle画圆形
import numpy as np
import matplotlib.pyplot as plt
x = y = np.arange(-4, 4, 0.1)
x,y = np.meshgrid(x, y)
plt.contour(x, y, x ** 2 + y ** 2, [9])
plt.axis("scaled")
plt.show()