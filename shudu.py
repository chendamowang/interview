# -*- coding: utf-8 -*-

"""
题目：写一个数独生成器，接受输入一个9 * 9 矩阵M（可为空），通过填充该矩阵，输出一个数独。
矩阵由以下符号表示：
‘*’ 表示 数字未知。
‘1-9’ 表示已知的数字。
"""

class SolveShudu(object):

    def __init__(self, shudu):
        self.s = shudu

    def check(self, i, j, value):
        """
        检查value是否允许填入self.s[i][j]
        :param i: int 第i行
        :param j: int 第j列
        :param value:int 填入self.s[i][j]的值
        :return: bool
        """

        #检查行是否满足要求
        if value in self.s[i]:
            return False

        #检查列是否满足要求
        if value in [self.s[k][j] for k in range(9)]:
            return False

        #检查九宫格是否满足要求
        for m in range(3):
            for n in range(3):
                if self.s[m+i//3*3][n+j//3*3] == value:
                    return False

        #都满足返回True
        return True

    def nextij(self):

        for i in range(9):
            for j in range(9):
                if self.s[i][j] == '*':
                    return i, j
        return -1,-1   #没有下一个未填项返回-1,-1

    def search(self):
        i,j = self.nextij()

        #没有下一个未填项返回 True,表示求解完成
        if i == -1 and j == -1:
            return  True

        #把可能的值填入未填项
        for value in range(1, 10):
            if self.check(i, j, value):
                self.s[i][j] = value  #检查通过把value填入self.s[i][j]
                if not self.search():
                    self.s[i][j] = '*'  #后面的检查未通过,回溯.把self.s[i][j]重新赋值为未知数：*
                else:
                    return True
        return False #所有可能值都填入失败,求解失败

if '__main__' == __name__:

    shudu1 = [['*', '*', '*', '*', '*', '*', '*', '*', '*'],
              ['*', '*', '*', '*', '*', '*', '*', '*', '*'],
              ['*', '*', '*', '*', '*', '*', '*', '*', '*'],
              ['*', '*', '*', '*', '*', '*', '*', '*', '*'],
              ['*', '*', '*', '*', '*', '*', '*', '*', '*'],
              ['*', '*', '*', '*', '*', '*', '*', '*', '*'],
              ['*', '*', '*', '*', '*', '*', '*', '*', '*'],
              ['*', '*', '*', '*', '*', '*', '*', '*', '*'],
              ['*', '*', '*', '*', '*', '*', '*', '*', '*']]

    shudu2 = [['*',  1 , '*', '*',  5 , '*', '*', '*', '*'],
              ['*', '*',  3 , '*', '*', '*',  5 ,  2 , '*'],
              ['*',  2 , '*',  6 , '*',  7 , '*', '*', '*'],
              [ 8 , '*',  1 , '*', '*',  9 , '*', '*', '*'],
              ['*', '*', '*', '*', '*', '*',  8 ,  3 ,  1 ],
              [ 5 , '*', '*', '*',  2 ,  1 , '*', '*', '*'],
              ['*',  6 ,  2 , '*', '*', '*', '*', '*',  8 ],
              [ 1 ,  8 , '*',  2 ,  9 , '*', '*', '*', '*'],
              ['*', '*', '*',  4 , '*', '*', '*',  6 ,  2 ]]


    s = SolveShudu(shudu1)
    s2 = SolveShudu(shudu2)
    s.search()
    s2.search()

    for i in shudu1:
        print i
    print '------------'
    for i in shudu2:
        print i