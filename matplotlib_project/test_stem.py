# coding=utf-8
# @FileName: test_stem.py
# @Author: ZhengQiang
# Date: 2019/12/30 10:04 上午

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.1, 2 * np.pi, 41)
y = np.exp(np.sin(x))

plt.stem(x, y, use_line_collection=True)
plt.show()
