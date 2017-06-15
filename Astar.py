# This program is to find the shortest path in the given map using A* algorithm

import math
import json

# open map file and read contents to lines
from queue import Queue

text_file = open("simple-map.txt")
lines = text_file.readlines()
text_file.close()

# The number of row and column in the map
columns = len(lines[0]) - 2  # columns are 6 in simple map file
rows = len(lines)-1  # rows are 5 in simple map file


# Initialize new cell
class Cell:
    def __init__(self, x, y):
        self.x = x  # x coordinate of cell
        self.y = y  # y coordinate of cell
        self.parent = None  # the parent cell of current cell
        self.g = 0  # the path move cost
        self.h = 0  # heuristic
        self.f = self.g + self.h  # f = g + f

        # initial cost
        type_r = lines[x][y]
        if type_r is "r":
            self.cost = 1
        if type_r is "f":
            self.cost = 2
        if type_r is "h":
            self.cost = 5
        if type_r is "m":
            self.cost = 10
        if type_r is "w":
            self.cost = math.inf


# Define a function to find neighbors of cell
def get_neighbors(cell: Cell) -> list:
    neighbors = []
    if cell.x != rows:
        neighbors.append(Cell(cell.x + 1, cell.y))
    if cell.x != 0:
        neighbors.append(Cell(cell.x - 1, cell.y))
    if cell.y != 0:
        neighbors.append(Cell(cell.x, cell.y - 1))
    if cell.y != columns:
        neighbors.append(Cell(cell.x, cell.y + 1))
    for n in neighbors:
        n.parent = cell
        n.g = n.cost + cell.g
    return neighbors


# reconstruct path
def reconstruct_path(current_cell):
    print("find path")
    path = []
    while current_cell is not None:
        coordinate = [current_cell.x, current_cell.y]
        path.append(coordinate)
        current_cell = current_cell.parent
    print(path)

    # output json array file
    json.dumps(path)

    return path



# This function is to find the Cell which has lowest f score in openSet
def lowest_score(test_set: list):
    if not (not test_set):
        winner = test_set[0]
        for temp in test_set:
            if temp.f < winner.f:
                return temp
            else:
                return winner
    else:
        return False


# Initialize start, goal, and current cell
start = Cell(1, 1)
goal = Cell(3, 4)

# Initialize openSet and closeSet
openSet = []
closeSet = []

# add start to openSet
openSet.append(start)

# Path finding
while not (not openSet):
    current = lowest_score(openSet)
    if current.x == goal.x and current.y == goal.y:
        reconstruct_path(current)
        break
    openSet.remove(current)
    closeSet.append(current)

    neighbor_list = get_neighbors(current)  # find neighbors of current cell

    for neighbor in neighbor_list:
        for passed in closeSet:
            if neighbor.x == passed.x and neighbor.y == passed.y:
                continue
        if neighbor not in openSet:
            openSet.append(neighbor)

print("no result")




