# -*- coding:UTF-8 -*-
# 输入某年某月某日，判断这一天是这一年的第几天？
ordinary_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

year = input("年")
month = input("月")
day = input("日")
num = 0
if year % 100 == 0 and year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
    for i in range(0, month):
        num = num + leap_month[i]
    num = num + day
else:
    for i in range(0, month):
        num = num + ordinary_month[i]
    num = num + day

print(num)

