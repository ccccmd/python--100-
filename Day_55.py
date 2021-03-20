# -*- coding:utf-8 -*-
# 取一个整数从右端开始的4～7位
a = 16
b = a >> 4
print(b)
c = ~(~0 << 4)
d = b & c
print(d)