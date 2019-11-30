"""
-------------------------------------------------------
Main
-------------------------------------------------------
Author:  Edmund Lui
ID:      160635540
Email:   luix5540@mylaurier.ca
Section: CP468
-------------------------------------------------------
"""
from aStarAlgorithm import aStar
"""
def main():
    fv = open("input.txt","r")
    for i in fv:
        if i.endswith("\n"):
            print(i[:-1])
        else:
            print(i)
            
            
    cols = 5
    rows = 5

    grid = []


    for _ in range(cols):
        grid.append([])
    for i in range(cols):
        for j in range(rows):
            s = spot(i,j,grid)
            grid[i].append(s)
    for i in range(cols):
        for j in range(rows):
            grid[i][j].addNeighbours(grid)
            
    
    start = grid[0][0]
    end = grid[cols-1][rows-1]
    
    solve = aStar(start,end)
    print(solve)
"""  
def main():

    grid = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 0, 1, 1]]

    start = (4, 2)
    end = (4, 7)

    path = aStar(grid, start, end)
    print(path)
    
main()
