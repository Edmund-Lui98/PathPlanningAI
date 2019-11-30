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


class spot():

    def __init__(self, prev=None, location=None):
        #previous location
        self.prev = prev
        #current location
        self.location = location
        #f, g, and h for A* algorithm
        self.f = 0
        self.g = 0
        self.h = 0
        

    def __eq__(self, other):
        return self.location == other.location
