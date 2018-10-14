# -*- coding: utf-8 -*-
from random import choice

class Game(object):
    def __init__(self, height=10, width=10, boom=15):
        self.height = height
        self.width = width
        self.boom = boom
        self.reset()

    #增加地雷
    def add_boom(self):
        for i in range(self.boom):
            (i, j) = choice([(i, j) for i in range(self.width) for j in range(self.height) if self.field[i][j] == '#'])
            self.field[i][j] = '*'

    #计算格子四周地雷数：0-8
    def add_num(self):
        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for i in range(self.width):
            for j in range(self.height):
                if self.field[i][j] != '*':
                    sum = 0
                    for k in range(8):
                        m = i + dirs[k][0]
                        n = j + dirs[k][1]
                        if self.width > m >= 0 and self.height > n >= 0 \
                                and self.field[m][n] == '*':
                            sum += 1
                        self.field[i][j] = sum

    def reset(self):
        # self.field实际的扫雷地图。 self.show显示的扫雷地图
        self.field = [['#' for i in range(self.width)] for j in range(self.height)]
        self.add_boom()
        self.add_num()
        self.show = [['#' for i in range(self.width)] for j in range(self.height)]

    #画出扫雷界面
    def draw(self):
        a =  '   ' + ''.join(' %d' % n for n in range(self.width))
        print a
        print '   ---------------------'

        for v in range(len(self.show)):
            a = '%d  ' % v
            for k in self.show[v]:

                if k == '#':
                    b = '|#'
                elif k == '*':
                    b = '|*'
                elif k == 0:
                    b = '| '
                else:
                    b = '|%d' % k
                a = a+b
            a = a+'|'
            print a
            self.draw_line()

    def draw_line(self):
        print '   ---------------------'

    def expand(self, x, y, seen):
        """
        扩展每次确认的点。周围没雷则继续扩展
        :param x: int 行数
        :param y: int 列数
        :param seen: list 被扩展过的点不再继续扩展
        """
        dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        if self.field[x][y] == 0:  #周围没雷向上下左右扩展
            self.show[x][y] = 0
            seen.append((x, y))
            for l in range(4):
                x_new = x + dirs[l][0]
                y_new = y + dirs[l][1]
                if self.height > x_new >= 0 and self.width > y_new >= 0\
                            and (x_new, y_new) not in seen:
                    self.expand(x_new, y_new, seen)
        else:   #扩展的数字或雷就直接显示
            self.show[x][y] = self.field[x][y]
            seen.append((x, y))

    #检查游戏是否胜利或失败
    def check(self):
        count = 0
        for row in self.show:
            for column in row:
                if column == '#':
                    count +=1
        if count == self.boom:
            return 'You win!!!'

        for row in self.show:
            if '*' in row:
                return 'Boom!!!! Gameover!!!'



    def start(self):
        self.draw()
        seen = []
        while True:
            note = self.check()
            if note == 'You win!!!':
                print 'You win!!!'
                break
            if note == 'Boom!!!! Gameover!!!':
                print 'Boom!!!! Gameover!!!'
                break

            try: #每次确认一个点
                x = int(raw_input('请输入行数：'))
                y = int(raw_input('请输入列数：'))
            except:
                raise TypeError('必须输入正整数')

            self.expand(x, y, seen)
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.start()
