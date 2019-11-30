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
import math
from spot import spot

def heuristic(neighbor, end):
    distance = math.sqrt( ((end.location[0]-neighbor.location[0])**2)+((end.location[1]-neighbor.location[1])**2) )
    return distance;

def aStar(grid, start, end):
    start = spot(None, start)
    end = spot(None, end)

    openSet = []
    closedSet = []

    openSet.append(start)

    while len(openSet) > 0:

        cur = openSet[0]
        cur_index = 0
        for index, item in enumerate(openSet):
            if item.f < cur.f:
                cur = item
                cur_index = index

        openSet.pop(cur_index)
        closedSet.append(cur)

        if cur == end:
            path = []
            current = cur
            while current is not None:
                path.append(current.location)
                current = current.prev
            return path[::-1] 

        neighbors = []
        for new_location in [(0, -1), (0, 1), (-1, 0), (1, 0)]: 
            # Get spot location
            spot_location = (cur.location[0] + new_location[0], cur.location[1] + new_location[1])

            # Make sure within range
            if spot_location[0] > (len(grid) - 1) or spot_location[0] < 0 or spot_location[1] > (len(grid[len(grid)-1]) -1) or spot_location[1] < 0:
                continue

            # Make sure walkable terrain
            if grid[spot_location[0]][spot_location[1]] != 0:
                continue

            # Create new spot
            new_spot = spot(cur, spot_location)

            # Append
            neighbors.append(new_spot)

        # Loop through neighbors
        for neighbor in neighbors:

            # neighbor is on the closed list
            for closed_neighbor in closedSet:
                if neighbor == closed_neighbor:
                    continue

            # Create the f, g, and h values
            neighbor.g = cur.g + 1
            neighbor.h = heuristic(neighbor, end)
            neighbor.f = neighbor.g + neighbor.h

            # neighbor is already in the open list
            for aSpot in openSet:
                if neighbor == aSpot and neighbor.g > aSpot.g:
                    continue

            # Add the neighbor to the open list
            openSet.append(neighbor)


