import math

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePathsRecurse(self, A, B):
        if A == 1 or B == 1:
            return 1
        paths = 0
        if B-1 > 0:
            paths += self.uniquePathsRecurse(A,B-1)
        if A-1 > 0:
            paths += self.uniquePathsRecurse(A-1, B)
        return paths
    
    def uniquePathsMath(self, A, B):
        down = A-1
        right = B-1 #M
        total_steps = down + right #N
        return math.factorial(total_steps) / (math.factorial(right) \
        * math.factorial(total_steps - right))
        
    def uniquePathsDP(self, A, B):
        grid = [[0 for X in range(B)] for x in range(A)]
        #set first row to zero
        for i in range(len(grid[0])):
            grid[0][i] = 1
        #set first col to zero
        for i in range(len(grid)):
            grid[i][0] = 1
        row = 1
        col = 1
        while row < A:
            i = col
            while i < B:
                above = grid[row-1][i]
                left = grid[row][i-1]
                grid[row][i] = above + left
                i+=1
            row+=1
        return grid[A-1][B-1]


sol = Solution()
print sol.uniquePathsRecurse(9, 15) == 319770
print sol.uniquePathsMath(9, 15) == 319770
print sol.uniquePathsDP(9, 15) == 319770