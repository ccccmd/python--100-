# -*- coding:UTF-8 -*-
# 判断一个数是否是回文数

string = input("请输入一个数字")
string_reverse = string[::-1]
if string == string_reverse:
    print("它是一个回文数")
else:
    print("它不是一个回文数")