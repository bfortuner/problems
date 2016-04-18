"""
Largest Connected Group

Given 2D array of X/-, find the size of the largest connected group of X's
	x x - -
	x - - -
	x - - x
	- - x -

	- x x -
	- x - -
	- x - x
	- - x -

Cases:
1) All X or -
2) Do diagnals count?
3) Two equal groups?
4) Group in the middle

Approach
1) DFS - Starting at top left, loop through 2x2 array and begin search
2) Keep track of nodes visited storing copy of array all 0s
3) Keep track of max size at the top
---
4) Three methods, 1 loops through, 1 DFS get size, which does a search if it finds an 'X' (marking elems as visited), 
1 get neighbors which gets all x neighbors

"""

def get_copy_of_matrix(matrix):
	copy = []
	for row in range(len(matrix)):
		copy.append([0 for x in range(len(matrix[0]))])
	return copy

def get_max_group_size(matrix):
	max_group_size = 0
	visited = get_copy_of_matrix(matrix)
	for row_no in range(len(matrix)):
		for col_no in range(len(matrix[0])):
			group_size = get_group_size(matrix, visited, row_no, col_no)
			max_group_size = max(group_size, max_group_size)
	return max_group_size

def get_group_size(matrix, visited, row_no, col_no):
	if matrix[row_no][col_no] == 0:
		return 0
	visited[row_no][col_no] = 1
	cur_sum = 1
	#up
	if row_no-1 >= 0 and visited[row_no-1][col_no] == 0:
		cur_sum += get_group_size(matrix, visited, row_no-1, col_no)
	#down
	if row_no+1 < len(matrix) and visited[row_no+1][col_no] == 0:
		cur_sum += get_group_size(matrix, visited, row_no+1, col_no)
	#left
	if col_no-1 >= 0 and visited[row_no][col_no-1] == 0:
		cur_sum += get_group_size(matrix, visited, row_no, col_no-1)
	#right
	if col_no+1 < len(matrix[0]) and visited[row_no][col_no+1] == 0:
		cur_sum += get_group_size(matrix, visited, row_no, col_no+1) 
	#edge of board and/or visited all adjacent nodes
	return cur_sum



#Tests

matrix=[
 [1,1,0,0],
 [1,0,0,0],
 [1,0,0,1],
 [0,0,1,0]
]

matrix2=[
 [1,0,1,0],
 [0,1,1,0],
 [0,1,0,1],
 [1,1,1,0]
]

matrix3=[
 [1,0,1],
 [0,1,1],
 [0,1,0]
]

matrix_copy=[
 [0,0,0,0],
 [0,0,0,0],
 [0,0,0,0],
 [0,0,0,0]
]

def get_matrix():
	return [
	 [1,1,0,0],
	 [1,0,0,0],
	 [1,0,0,1],
	 [0,0,1,0]
	]

def get_matrix2():
	return [
	 [1,0,1,0],
	 [0,1,1,0],
	 [0,1,0,1],
	 [1,1,1,0]
	]

def test_get_visited():
	assert get_copy_of_matrix(matrix) == matrix_copy

def test_get_group_size():
	assert get_group_size(get_matrix(), get_copy_of_matrix(get_matrix()), 0, 0) == 4
	assert get_group_size(get_matrix(), get_copy_of_matrix(get_matrix()), 2, 3) == 1
	assert get_group_size(get_matrix(), get_copy_of_matrix(get_matrix()), 3, 2) == 1
	assert get_group_size(get_matrix2(), get_copy_of_matrix(get_matrix2()), 0, 0) == 1
	assert get_group_size(get_matrix2(), get_copy_of_matrix(get_matrix2()), 0, 2) == 7

def test_get_max_group_size():
	assert get_max_group_size(get_matrix()) == 4
	assert get_max_group_size(get_matrix2()) == 7
	assert get_max_group_size(matrix3) == 4

if __name__ == "__main__":
	test_get_visited()
 	test_get_group_size()
 	test_get_max_group_size()