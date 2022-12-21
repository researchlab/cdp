"""角谷猜想"""

""""
【问题描述】
    日本的角谷提出了一个猜想, 对于任意的自然数，反复进行如下运算：
    (1)若为奇数，则乘以3后加1;
    (2)若为偶数，则除以2;
    总可以得到运算结果1
"""

def jiaogu(n):
    nc = n 
    while nc != 1:
        nc = nc * 3 + 1 if nc % 2 else nc /2 

    print('%d 符合角谷猜想' % n)

jiaogu(18)
