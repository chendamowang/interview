# -*- coding: utf-8

"""
题目: 写一个 tree.py, 通过 python tree.py 模拟实现linux 命令行 tree 的输出
"""

import os
from sys import argv

if len(argv) < 2:
    path = os.getcwd()
else:
    path = argv[1]


def tree(path, deep=0):
    a =  '|    '*deep + '|----'
    for i in os.listdir(path):
        print a + i
        subdir = os.path.join(path, i)
        if os.path.isdir(subdir):
            tree(subdir, deep + 1)

if __name__ == '__main__':
    tree(path)
