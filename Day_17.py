# -*- coding:UTF-8 -*-
# 输入一行字符，分别统计出其中英文字母、空格、数字和其他字符的个数

s = input("请输入字符")
letters = 0
space = 0 
num = 0
other = 0

for i in s:
    if i.isalpha():
        letters += 1
    elif i.isspace():
        space += 1
    elif i.isdigit():
        num += 1
    else:
        other += 1

print(letters, space, num, other)