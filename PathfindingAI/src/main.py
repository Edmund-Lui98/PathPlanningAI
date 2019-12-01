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

def print_grid(grid,path):
    for j in path:
        p = j[0]
        q = j[1]
        grid[q][p] = "*"
    for i in grid:
        print()
        for j in i:
            print (j,end = "")
    for j in path:
        p = j[0]
        q = j[1]
        grid[q][p] = 0
    print()
    print()
def main():
    #opening input file
    fv = open("input.txt","r")
    
    #defining variables to make the grid
    cols = 0
    rows = 0
    num_of_robots = 0
    robot_locations = []
    grid = []
    end = (0,0)
    
    
    #going through file and extracting data
    x = 0
    for i in fv:
        z = i[:-1]
        #cols and rows
        if x == 0:
            values = z.split(" ")
            rows = int(values[0])
            cols = int(values[1])
        #number of robots
        elif x == 1:
            num_of_robots = int(z) + x
        #locations of robot
        elif x <= num_of_robots:
            values = z.split(" ")
            a = int(values[0])
            b = int(values[1])
            robot_locations.append((a,b))
        elif x == num_of_robots + 1:
            values = z.split(" ")
            a = int(values[0])
            b = int(values[1])
            end = (a,b)
        else:
            temp_grid = []
            for j in z:
                temp_grid.append(int(j))
            grid.append(temp_grid)
        x += 1
         
    
    for i in robot_locations:
        path = aStar(grid,i,end)
        print(path)
        new_grid = grid
        print_grid(new_grid, path)
    
    

main()
