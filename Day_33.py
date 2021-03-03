# -*- coding:utf-8 -*-
# 按逗号分割列表当中的元素
lst = [1, 3, 4, 5]
s = ','.join(str(n) for n in lst)
print(s)