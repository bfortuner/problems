"""
Find sqrt of number in log(n) time
"""

class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        L = 0
        H = A
        while L<=H:
            M = L + (H-L)/2
            sqrt = self.get_sqrt_candidate(M,A)
            if sqrt is not None:
                return sqrt
            elif M*M < A:
                L = M+1
            else:
                H = M-1
        return -1
    
    def get_sqrt_candidate(self, num, A):
        if num*num == A:
            return num
        elif (num+1)*(num+1) == A:
            return num+1
        elif num*num < A and (num+1)*(num+1)>A:
            return num
        return None

sol = Solution()

print sol.sqrt(11) == 3
print sol.sqrt(1) == 1
print sol.sqrt(0) == 0
print sol.sqrt(9) == 3
print sol.sqrt(4) == 2