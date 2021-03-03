# -*- coding:utf-8 -*-
# 利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来
str = input("输入字符")
def f(x):
    if x == -1:
        return ''
    return str[x] + f(x - 1)
print(f(len(str) - 1))