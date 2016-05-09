"""
Write an efficient algorithm that searches for a value in an m x n matrix.

This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than or equal to the last integer of the previous row.
Example:

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return 1 ( 1 corresponds to true )

Return 0 / 1 ( 0 if the element is not present, 1 if the element is present ) for this problem

"""

class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        if len(A) < 1:
            return 0
        rows = len(A)
        cols = len(A[0])
        L = 0
        H = rows * cols
        while L <= H:
            M = L + (H-L)/2
            row = (M-1) / cols
            col = (M-1) % cols
            val = A[row][col]
            if val == B:
                return 1
            elif val < B:
                L = M+1
            else:
                H = M-1
        return 0


sol = Solution()

matrix = [
[1, 3, 5, 7],
[10,11,16,20],
[23,30,54,60]]

print sol.searchMatrix(matrix,10) == 1
print sol.searchMatrix(matrix,13) == 0
print sol.searchMatrix(matrix,-1) == 0