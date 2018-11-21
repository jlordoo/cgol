import numpy
import random
import time

class Life:
    line = lambda s : [[(1 if (row == s//2 and spot in range(s//2-5,s//2+5)) else 0) for spot in range(s)] for row in range(s)]
    glider = lambda s : [[(1 if (row == s//2 - 1 and spot == s//2) or (row == s//2 and spot == s//2 + 1) or (row == s//2 + 1 and spot in range(s//2-1,s//2+2)) else 0) for spot in range(s)] for row in range(s)]
    def __init__(self, s = 60, m = 1000, start = []):
        self.s = s
        self.m = m
        self.new = numpy.zeros(s*s, dtype='i').reshape(s,s)
        if numpy.sum(start)>0:
            self.old = start
        else:
            self.old = [[(1 if random.randint(0, 99) < 10 else 0) for spot in range(s)] for row in range(s)]
                    
    def live_n(self, x, y):
        n = 0
        for dx in (-1,0,1):
            for dy in (-1,0,1):
                if dx == dy == 0:
                    continue
                if x+dx == self.s or y+dy == self.s:
                    if x+dx == self.s and y+dy != self.s:
                        n+=self.old[0][y+dy]
                    elif x+dx != self.s and y+dy == self.s:
                        n+=self.old[x+dx][0]
                    else:
                        n+=self.old[0][0]
                    continue
                n+=self.old[x+dx][y+dy]
        return n

    def game(self):
        '''
        1. Any live cell with fewer than two live neighbors dies, as if by underpopulation.
        2. Any live cell with two or three live neighbors lives on to the next generation.
        3. Any live cell with more than three live neighbors dies, as if by overpopulation.
        4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
        '''
        t = 1 
        while t <= self.m:
            grid = ''
            for x in range(self.s):
                for y in range(self.s):
                    if bool(self.old[x][y]):
                        grid+='■ '
                    else:
                        grid+='  '
                grid+='\n'
            print(grid)
            time.sleep(.5)
            print(chr(27) + "[2J")
            
            for x in range(self.s):
                for y in range(self.s):
                    alive = bool(self.old[x][y])
                    n = self.live_n(x,y)
                    if alive and n < 2:
                        self.new[x][y] = 0
                    elif alive and (n == 2 or n == 3):
                        self.new[x][y] = 1
                    elif alive and n > 3:
                        self.new[x][y] = 0
                    elif not alive and n == 3:
                        self.new[x][y] = 1
                    
            self.old = self.new.copy()
            
            t+=1
