"""
SetMatrixToZero

If an element in a M x N matrix is zero, set its entire row and column to zero

Cases
1) BAD INPUT - Empty matrix
2) BAD INPUT - Not a matrix [1,2,3,4]
3) One element - [[1]]
4) No zeros - [[1,3],
			   [1,2]]
5) All zeros - [[0,0],
			    [0,0]]
6) Multiple zero same row
7) Multiple zero same col

Approach
1) Store two sets, rows_to_zero, cols_to_zero
2) Loop through matrix, if find zero, add row + col to Sets_To_Zero
3) Create Two Helper method, set_row_to_zero(row_no), set_col_to_zero(col_no)
4) Loop through row_to_zero, call helper
5) Loop through col_to_zero, call helper
"""


def set_matrix_to_zero(matrix):
	rows_to_zero = set()
	cols_to_zero = set()
	for row in range(len(matrix)):
		for col in range(len(matrix[0])):
			if matrix[row][col] == 0:
				if row not in rows_to_zero:
					rows_to_zero.add(row)
				if col not in cols_to_zero:
					cols_to_zero.add(col)
	for row_no in rows_to_zero:
		set_row_to_zero(matrix, row_no)
	for col_no in cols_to_zero:
		set_col_to_zero(matrix, col_no)
	return matrix

def set_row_to_zero(matrix, row_no):
	for col_no in range(len(matrix[row_no])):
		matrix[row_no][col_no] = 0

def set_col_to_zero(matrix, col_no):
	for row_no in range(len(matrix)):
		matrix[row_no][col_no] = 0


# Tests

m1 = [
[1,0,0,1],
[0,1,1,1],
[1,1,1,1],
[1,1,1,1]]

a1 = [
[0,0,0,0],
[0,0,0,0],
[0,0,0,1],
[0,0,0,1]
]


def test_set_matrix_to_zero():
	assert set_matrix_to_zero(m1) == a1

if __name__ == "__main__":
	test_set_matrix_to_zero()