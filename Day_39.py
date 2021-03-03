# -*- coding:utf-8 -*-
# 按顺序，在原有的数列当中，插入一个新的数，序列规律保持不变，如何实现？
lst = [1,2,4,5,7,9,11,13,17]
n = input()
lst.append(n)
lst.sort()
print(lst)