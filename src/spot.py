"""
-------------------------------------------------------
Spot class
-------------------------------------------------------
Author:  Edmund Lui
ID:      160635540
Email:   luix5540@mylaurier.ca
Section: CP164
__updated__ = "2018-08-"
-------------------------------------------------------
"""


class spot:
    def __init__(self,x,y,grid):
        self.x = x
        self.y = y
        self.f = 0
        self.g = 0
        self.h = 0
        self.neighbours = []
        self.prev = None
        
        self.cols = 5
        self.rows = 5
        
    def addNeighbours(self,grid):
        if self.x < self.cols-1:
            self.neighbours.append(grid[self.x+1][self.y])
        if self.x > 0:
            self.neighbours.append(grid[self.x-1][self.y])
        if self.y < self.rows-1:
            self.neighbours.append(grid[self.x][self.y+1])
        if self.y > 0:
            self.neighbours.append(grid[self.x][self.y-1])
        