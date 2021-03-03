# -*- coding:UTF-8 -*-
# 输入首字母判断是星期几

# M T W T F S S

string = input("请输入首字母")
week = ['M', 'TU', 'W', 'TH', 'F', 'SA', 'SU']
if string in week:
    print("星期%d" %(week.index(string) + 1))
elif string in ['T', 'S']:
    string2 = input("请输入第二个字母")
    string = string + string2
    if string in week:
        print("星期%d" %(week.index(string) + 1))
