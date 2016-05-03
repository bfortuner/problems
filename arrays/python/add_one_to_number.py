"""
Given a non-negative number represented as an array of digits,

add 1 to the number ( increment the number represented by the digits ).

The digits are stored such that the most significant digit is at the head of the list.

Example:

If the vector has [1, 2, 3]

the returned vector should be [1, 2, 4]

as 123 + 1 = 124.

CASES:
---------
[] = [1]
[1] = [2]
[0 0 0] = [1]
[9 9 9] = [1 0 0 0]
[1 2 3] = [1 2 4]
[0 1 2 3] = [1 2 4]
"""

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        if len(A) == 0:
            return [1]
        i = len(A)-1
        found = False
        while i >= 0:
            if A[i] == 9:
                A[i] = 0
                i -= 1
            else:
                A[i] += 1
                found = True
                break
        if not found:
            return [1] + A
        i = 0
        while A[i] == 0:
            i += 1
        return A[i:]
