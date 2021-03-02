# -*- coding:utf-8 -*-
# 有一分数序列:2/1,3/2,5/3,8/5,13/8...求这个序列前20项的和
lst = []
sum = 0
a = 1
b = 2
for i in range(20):
    sum += float(b) / float(a)
    a, b = b, a + b
print(sum)

print((float(5) / float(3)))
# def fibnoici(n):
#     if n == 1:
#         return 2
#     if n == 2:
#         return 3
#     return fibnoici(n - 1) + fibnoici(n - 2)
# def bifnoici(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     return fibnoici(n - 1) + fibnoici(n - 2)
