# -*- coding: utf-8

"""
题目：输入一个整数 k (k < 50), 输出一个 k*k 的九宫图
"""

from random import shuffle

def creat_num(k):
    print str(k)+'*'+str(k)
    num_all = [i+1 for i in range(k*k)]
    shuffle (num_all)
    i = 1
    
    for num in num_all:
        if i < k:
            print '%02d' % num,
            i += 1
        else:
            print '%02d' % num
            i = 1

if __name__ == '__main__':

    try:
        k = int(raw_input('请输入正整数k:'))
        if k > 0:
            creat_num(k)
    except:
        print '您输入的数不合法。'
