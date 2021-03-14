# -*- coding:utf-8 -*-
# 比较数字大小

if __name__ == "__main__":
    a = float(input())
    b = float(input())
    if a > b:
        print("%.2f 大于 %.2f"%(a, b))
    
    if a == b:
        print("%.2f 等于 %.2f"%(a, b))

    if a < b:
        print("%.2f 小于 %.2f"%(a, b))