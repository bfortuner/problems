class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        res = []
        i = 0
        while i <= A:
            res = self.compute_next(res)
            res += [1]
            i += 1
        return res
            
    def compute_next(self, A):
        prior_num = 0
        for i in range(len(A)):
            cur_num = prior_num + A[i]
            prior_num = A[i]
            A[i] = cur_num
        return A