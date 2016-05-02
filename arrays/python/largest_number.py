"""
Given a list of non negative integers, arrange them such that they form the largest number.

For example:

Given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
"""

class Solution:
    # @param A : tuple of integers
    # @return a strings
    def get_list_from_tuple(self, tup):
    	l1 = []
    	for i in range(len(tup)):
    		l1.append(tup[i])
    	return l1

    def convert_to_str(self, A):
		string = ""
		for num in A:
			string += str(num)
		return string

    def largestNumber(self, A):
    	if A.count(0) == len(A):
    		return "0"
    	A = self.get_list_from_tuple(A)
    	for i in range(len(A)):
    		k = i
    		while k > 0:
    			if self.greater_or_equal(A[k],A[k-1]):
    				tmp = A[k]
    				A[k] = A[k-1]
    				A[k-1] = tmp
    				k-=1
    			else:
    				break
    	return self.convert_to_str(A)

    def greater_or_equal(self, num1, num2):
		if num1 == num2:
			return True
		a_str = str(num1)
		b_str = str(num2)
		a_greater_option = int(a_str + b_str)
		b_greater_option = int(b_str + a_str)
		return a_greater_option >= b_greater_option


sol = Solution()

def test_greater():
	assert sol.greater_or_equal(34, 3) == True
	assert sol.greater_or_equal(30, 3) == False
	assert sol.greater_or_equal(3, 30) == True
	assert sol.greater_or_equal(3, 3) == True
	assert sol.greater_or_equal(0, 0) == True
	assert sol.greater_or_equal(9, 5) == True
	assert sol.greater_or_equal(5, 9) == False

def test_largest_number():
	print sol.largestNumber((3,30,34,5,9))
	print sol.largestNumber((3,))
	print sol.largestNumber((9, 99, 999, 9999, 9998))
	print sol.largestNumber((0,0,0,0,0))

if __name__ == "__main__":
	test_greater()
	test_largest_number()