"""
Given a list of non negative integers, arrange them such that they form the largest number.

For example:

Given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
"""


class CompareNode:
	def __init__(self, val):
		self.val = str(val)

	def __gt__(self, other):
		a_greater_option = self.val + other.val
		b_greater_option = other.val + self.val
		return a_greater_option > b_greater_option

class Solution:
    # @param A : tuple of integers
    # @return a strings
    def get_list_from_tuple(self, tup):
    	l1 = []
    	for i in range(len(tup)):
    		l1.append(CompareNode(tup[i]))
    	return l1

    def convert_to_str(self, A):
		string = ""
		for node in A:
			string += str(node.val)
		return string

    def largestNumber(self, A):
    	if A.count(0) == len(A):
    		return "0"
    	A = self.get_list_from_tuple(A)
    	A.sort(reverse=True)
    	return self.convert_to_str(A)


sol = Solution()

def test_largest_number():
	print sol.largestNumber((3,30,34,5,9))
	print sol.largestNumber((3,))
	print sol.largestNumber((9, 99, 999, 9999, 9998))
	print sol.largestNumber((0,0,0,0,0))

if __name__ == "__main__":
	test_largest_number()