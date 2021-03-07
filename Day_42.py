# -*- coding:utf-8 -*-
# Python模仿静态变量实例
class Num:
    nNum = 1
    def inc(self):
        self.nNum += 1
        print("nNum=%d"%self.nNum)

if __name__ == '__main__':
    nNum = 2
    inst = Num()
    for i in range(3):
        nNum += 1
        print("nNum%d"%nNum)
        inst.inc()