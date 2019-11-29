"""
-------------------------------------------------------
A* algorithm implementation 
-------------------------------------------------------
Author:  Edmund Lui
ID:      160635540
Email:   luix5540@mylaurier.ca
Section: CP4684
-------------------------------------------------------
"""
def heuristic(neighbour, end):
    #distance = math.sqrt( ((end[0]-neighbour[0])**2)+((end[1]-neighbour[1])**2) )
    distance = abs(neighbour.x-end.x) + abs(neighbour.y-end.y)
    return distance;
         
def aStar(start, end):
    openSet = [start]
    closedSet = []
    path = []
    
    while len(openSet) > 0:
        lowest = 0;
        for i in range(len(openSet)):
            if (openSet[i].f < openSet[lowest].f):
                lowest = i
                
        current = openSet[lowest]
        if (current == end):
            temp = current
            path.append(temp)
            while temp.prev:
                path.append(temp.prev)
                temp = temp.prev
            print("done")
            return;
        
        openSet.remove(current)
        closedSet.append(current)
        
        for neighbour in current.neighbours:
            if neighbour in closedSet:
                tempG = current.g + 1 
                
                if neighbour in openSet:
                    if tempG < neighbour.g:
                        neighbour.g = tempG
                else:
                    neighbour.g = tempG
                    openSet.append(neighbour)
                    
                neighbour.h = heuristic(neighbour, end)
                neighbour.f = neighbour.g + neighbour.h
                neighbour.prev
                
    return path;
    