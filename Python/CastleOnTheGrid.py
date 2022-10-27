#!/bin/python3
# Name: Lucas Pavanelli
# Date: 26/10/2022

import math
import os
import random
import re
import sys
import queue

#
# Complete the 'minimumMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY grid
#  2. INTEGER startX
#  3. INTEGER startY
#  4. INTEGER goalX
#  5. INTEGER goalY
#

def minimumMoves(grid, startX, startY, goalX, goalY):
    def check_move(x, y):
        return x >= 0 and y >= 0 and x < len(grid) and y < len(grid) and grid[x][y] == '.'

    # IDEA 1 - we can use a queue to store positions to be visited
    # IDEA 2 - add to the queue all possible position along the current direction
    if startX == goalX and startY == goalY:
        return 0
    q = queue.Queue()
    visited = set()
    q.put((startX, startY, 0))
    visited.add((startX, startY))
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while not q.empty():
        cur_x, cur_y, num_moves = q.get()
        for dir_x, dir_y in directions:
            next_x = cur_x + dir_x
            next_y = cur_y + dir_y
            while check_move(next_x, next_y):
                if (next_x, next_y) not in visited:
                    if next_x == goalX and next_y == goalY:
                        return num_moves + 1
                    q.put((next_x, next_y, num_moves + 1))
                    visited.add((next_x, next_y))
                next_x = next_x + dir_x
                next_y = next_y + dir_y
    return -1
    
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    first_multiple_input = input().rstrip().split()

    startX = int(first_multiple_input[0])

    startY = int(first_multiple_input[1])

    goalX = int(first_multiple_input[2])

    goalY = int(first_multiple_input[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    fptr.write(str(result) + '\n')

    fptr.close()
