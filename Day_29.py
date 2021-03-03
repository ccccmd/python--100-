# -*- coding:utf-8 -*-
# 给一个不多于5位的正整数，求它是几位数，逆序打印出各位数字

n = input("请输入一个不多于5位的正整数")
print("这是一个%d位数" %len(n))
for i in range(len(n) - 1, -1, -1):
    print(n[i], end="")