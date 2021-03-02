# -*- coding:UTF-8 -*-
# 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第十次落地时共经过多少米？
# 第十次反弹多高？
# 100 ，50 50， 25 25 
lst = []
init = 100
lst.append(init)
for i in range(1,10):
    init = float(init / 2)
    lst.append(init)
    lst.append(init)
print(sum(lst))
print(float(init/2))

