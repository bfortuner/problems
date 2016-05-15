
"""
Connected Cells

Find the largest group of connected cells in a matrix of 0s and 1s.
Two cells are said to be connected if they are adjacent horizontally,
vertically, or diagonally.

input = [
[1,1,0,1,0],
[0,1,1,0,0],
[0,0,1,0,1],
[1,0,0,0,1],
[0,1,0,1,1]
]
output = 6

"""


"""
Dynamic Programming Solution
O(Row x Col) time
O(1) space
"""

def largest_group(matrix):
    max_group = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 1:
                localmax = 1
                directions = get_eligible_directions_dp(matrix, row, col)
                for dir in directions:
                    r2 = row+dir[0]
                    c2 = col+dir[1]
                    localmax += matrix[r2][c2]
                    matrix[r2][c2] = 0
                matrix[row][col] = localmax
                if localmax > max_group:
                    max_group = localmax
    return max_group

def get_eligible_directions_dp(m, row, col):
    directions = [(-1,-1),(-1,0),(-1,1),(0,-1)]
    eligible = []
    for dir in directions:
        r2 = row+dir[0]
        c2 = col+dir[1]
        if r2 < 0 or c2 < 0:
            continue
        elif c2 >= len(m[row]) or r2 >= len(m):
            continue
        eligible.append(dir)
    return eligible


"""
Naive Approach ----------

O((row*col)^2) time
O(1) space
"""

def largest_group_naive(matrix):
    max_group = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            groupsize = get_max_group(matrix, row, col)
            if groupsize > max_group:
                max_group = groupsize
    return max_group

def get_max_group(m, row, col):
    if row < 0 or row >= len(m):
        return 0
    if col < 0 or col >= len(m[row]):
        return 0
    if m[row][col] == 0:
        return 0
    m[row][col] = 0    ## Mark node as visited
    sum = 1
    directions = [(-1,-1),(-1,0),(-1,1),(1,1),(1,0),(0,1),(1,-1),(0,-1)]
    for dir in directions:
        sum += get_max_group(m, row+dir[0], col+dir[1])
    return sum    


matrix = [
[1,1,0,1,0],
[0,1,1,0,0],
[0,0,1,0,1],
[1,0,0,0,1],
[0,1,0,1,1]
]

print largest_group(matrix) == 6

matrix = [
[1,1,0,1,0],
[0,1,1,0,0],
[1,0,1,0,1],
[1,0,0,0,1],
[0,1,0,1,1]
]

print largest_group_naive(matrix) == 9
