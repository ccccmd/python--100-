# -*- coding:utf-8 -*-
# 暂停1s输出，并格式化当前时间

import time
for i in range(10):
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    time.sleep(1)