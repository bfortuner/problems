"""
Return the # of occurances of B
in the sorted Array A in log(n) time
"""

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def getFirstOccur(self, A, B):
        low = 0
        high = len(A)-1

        while low <= high:
            mid = low + (high-low)/2
            if A[mid] >= B:
                high = mid-1
            else:
                low = mid+1
        if low >= len(A):
            return None
        return low   
    
    def getLastOccur(self, A, B, low):
        high = len(A)-1

        while low <= high:
            mid = low + (high-low)/2
            if A[mid] > B:
                high = mid-1
            else:
                low = mid+1
        return high        
    
    def findCount(self, A, B):
        lowerBound = self.getFirstOccur(A,B)
        if lowerBound is None:
            return None
        higherBound = self.getLastOccur(A,B,lowerBound)
        
        return higherBound-lowerBound+1


sol = Solution()

print sol.findCount([1,2,3,3,3,4,5,5,6,7,8], 3) == 3
print sol.findCount([1],3) == None
print sol.findCount([1],1) == 1
print sol.findCount([1,1],1) == 2
print sol.findCount([1,2],1) == 1
