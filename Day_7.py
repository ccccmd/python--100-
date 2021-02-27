# -*- coding:utf-8 -*-
# 将一个列表的数据复制到另一个列表中

a = input()
item = a.split(" ")
list1 = [eval(x) for x in item]
list2 = list1[:]
print(list2)