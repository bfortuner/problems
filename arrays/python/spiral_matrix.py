"""
Print Spiral matrix

2 4 6 8
5 9 12 16
2 11 5 9
3 2 1 8

print:
2 4 6 8 16 9 8 1 2 3 2 5 9 12 5 11

"""

class Tile(object):
	"""
	row = height of matrix
	column = width of matrix
	"""

	def __init__(self, row, column):
		self.row = row
		self.column = column

def copy_matrix(matrix):
	rows = len(matrix)
	columns = len(matrix[0])
	return [[None for column in range(columns)] \
	for row in range(rows)]

def get_next_direction(cur_dir):
	directions = {
		"R":"D",
		"D":"L",
		"L":"U",
		"U":"R"
	}
	return directions[cur_dir]

def get_next_tile(tile, cur_dir, visited):
	if cur_dir == "R":
		next_tile = Tile(tile.row, tile.column+1)
	elif cur_dir == "D":
		next_tile = Tile(tile.row+1, tile.column)
	elif cur_dir == "L":
		next_tile = Tile(tile.row, tile.column-1)
	elif cur_dir == "U":
		next_tile = Tile(tile.row-1, tile.column)

	#validation here!
	if next_tile.row >= len(visited) or next_tile.row < 0:
		return None
	if next_tile.column >= len(visited[next_tile.row]) or next_tile.column < 0:
		return None

	#visited check here!
	if visited[next_tile.row][next_tile.column] is not None:
		return None #we already visited

	return next_tile

"""
2 4 6 8
5 9 12 16
2 11 5 9
3 2 1 8
"""

def print_spiral(matrix):
	visited = copy_matrix(matrix)
	tile = Tile(0,0)
	cur_dir = "R"
	next_dir = get_next_direction(cur_dir)
	while tile is not None:
		print matrix[tile.row][tile.column]
		visited[tile.row][tile.column] = 1
		if get_next_tile(tile, cur_dir, visited) is not None:
			tile = get_next_tile(tile, cur_dir, visited)
		elif get_next_tile(tile, next_dir, visited) is not None:
			tile = get_next_tile(tile, next_dir, visited)
			cur_dir = next_dir
			next_dir = get_next_direction(cur_dir)
		else:
			tile = None



matrix1 = [
[2,4,6,8],
[5,9,12,16],
[2,11,5,9],
[3,2,1,8]]

def test_copy_matrix():
	assert copy_matrix([[1,1],[1,1]]) \
	== [[None,None],[None,None]]

def test_get_next_tile():
	visited = [[None,None,None],[None,None,None],[None,None,None]]
	t1 = get_next_tile(Tile(0,0), "R", visited)
	assert t1.row == 0
	assert t1.column == 1

	t1 = get_next_tile(Tile(0,2), "R", visited)
	assert t1 == None

	t1 = get_next_tile(Tile(0,2), "D", visited)
	assert t1.row == 1
	assert t1.column == 2

	visited = [ [None,None,None],
				[None,None,1],
				[None,None,None]]
	t1 = get_next_tile(Tile(0,2), "D", visited)
	assert t1 == None  # already visited

	t1 = get_next_tile(Tile(2,2), "D", visited)
	assert t1 == None

	t1 = get_next_tile(Tile(2,2), "L", visited)
	assert t1.row == 2
	assert t1.column == 1

	t1 = get_next_tile(Tile(2,0), "L", visited)
	assert t1 == None
	
	t1 = get_next_tile(Tile(2,0), "U", visited)
	assert t1.row == 1
	assert t1.column == 0

	visited = [ [1,None,None],
				[None,None,1],
				[None,None,None]]
	t1 = get_next_tile(Tile(1,0), "U", visited)
	assert t1 == None # already visited

	t1 = get_next_tile(Tile(1,0), "R", visited)
	assert t1.row == 1
	assert t1.column == 1

def test_print_spiral():
	print_spiral(matrix1)
	print_spiral([[0]])
	print_spiral([[0,0],[0,0]])
	print_spiral([[1,2,3,4],[1,2,3,4]])
	print_spiral([[1,2],[3,4],[5,6]])


if __name__ == "__main__":
	test_copy_matrix()
	test_print_spiral()
	test_get_next_tile()
