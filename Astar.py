# This program is to find the shortest path in the given map using A* algorithm

# open map file and read contents to lines
from queue import Queue

text_file = open("simple-map.txt")
lines = text_file.readlines()
text_file.close()

# The number of row and column in the map
columns = len(lines[0]) - 1  # columns are 6 in simple map file
rows = len(lines)  # rows are 5 in simple map file

# initial closeSet and openSet
closeSet = []
openSet = Queue()

# Initialize new cell
class Cell(object):
    def __init__(self, x, y):
        self.x = x  # x coordinate of cell
        self.y = y  # y coordinate of cell
        self.parent = None # the parent cell of current cell
        self.g = 0  # the path move cost
        self.h = 0  # heuristic
        self.f = self.g + self.h  # f = g + f

# Define a function to find neighbors of cell
def get_neighbors(self, Cell)
    neighbors = []
    if Cell.x

# Initialize start, goal, and current cell
start = Cell
start.x = 0
start.y = 0

goal = Cell
goal.x = 4
goal.y = 4


