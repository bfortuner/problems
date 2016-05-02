"""
Pascals Rows

Given numRows, generate the first numRows of Pascal's triangle.

Pascal's triangle : To generate A[C] in row R, sum up A'[C] and A'[C-1] from previous row R - 1.

Example:

Given numRows = 5,

Return

[
     [1],
     [1,1],
     [1,2,1],
     [1,3,3,1],
     [1,4,6,4,1]
]
input = 9
 [1 ] 
 [1 1 ] 
 [1 2 1 ] 
 [1 3 3 1 ] 
 [1 4 6 4 1 ] 
 [1 5 10 10 5 1 ] 
 [1 6 15 20 15 6 1 ] 
 [1 7 21 35 35 21 7 1 ] 
 [1 8 28 56 70 56 28 8 1 ]


Observations
 1) input 9, ouput 9 arrays
 2) each output arry is a mirror image of itself forward and backwards

"""

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generate(self, A):
        if A == 0:
            return []
        out = [[1]]
        for i in range(1,A):
            row = [1]
            k = 1
            while k < i:
                row.append(out[-1][k-1] + out[-1][k])
                k+=1
            row.append(1)
            out.append(row)
        return out

sol = Solution()
assert sol.generate(5) == [
     [1],
     [1,1],
     [1,2,1],
     [1,3,3,1],
     [1,4,6,4,1]
]