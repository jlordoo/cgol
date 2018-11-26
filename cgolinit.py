import random
import time
from math import inf
from copy import deepcopy

class Life:
    
    line = lambda r,c : [[(1 if (row == r//2 and spot in range(r//2-5,r//2+5)) else 0) for spot in range(c)] for row in range(r)]
    glider = lambda r,c : [[(1 if (row == r//2 - 1 and spot == r//2) or (row == r//2 and spot == r//2 + 1) or (row == r//2 + 1 and spot in range(r//2-1,r//2+2)) else 0) for spot in range(c)] for row in range(r)]
    
    
    def __init__(self, rows = 60, cols = 60, m = inf, speed = 0.3, percent = 10, start = []):
        self.rows = rows
        self.cols = cols
        self.m = m
        self.speed = speed
        self.new = [[0 for cell in range(cols)] for row in range(rows)] 
        if start:
            self.old = start
        else:
            self.old = [[(1 if random.randint(0, 99) < percent else 0) for spot in range(cols)] for row in range(rows)]
                    
    def live_n(self, x, y):
        n = 0
        for dx in (-1,0,1):
            for dy in (-1,0,1):
                if dx == dy == 0:
                    continue
                if x+dx == self.rows or y+dy == self.cols:
                    if x+dx == self.rows and y+dy != self.cols:
                        n+=self.old[0][y+dy]
                    elif x+dx != self.rows and y+dy == self.cols:
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
        g = 1 
        while g <= self.m:
            grid = ''
            for x in range(self.rows):
                for y in range(self.cols):
                    if bool(self.old[x][y]):
                        grid+='■ '
                    else:
                        grid+='  '
                grid+='\n'
            print(grid)
            print("Generation",g)
            time.sleep(self.speed)
            print(chr(27) + "[2J")
            
            for x in range(self.rows):
                for y in range(self.cols):
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
                    
            self.old = deepcopy(self.new)
            
            g+=1
