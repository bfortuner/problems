class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference. 
    # You do not need to return anything in this case. 
    def arrange(self, A):
        i = 0
        while i < len(A):
            if i == A[i]:
                i+=1
            else:
                tmp = A[i]
                A[i] = A[tmp]
                A[tmp] = tmp

    def arrangeRecursive(self, A):
        self.recurse(A, 0)
        
    def recurse(self, A, cur_index):
        if cur_index >= len(A):
            return
        override = A[A[cur_index]]
        self.recurse(A,cur_index+1)
        A[cur_index] = override
        return

sol = Solution()

A = [4,0,2,1,3]
sol.arrange(A)
print A

A = [4,0,2,1,3]
sol.arrangeRecursive(A)
print A