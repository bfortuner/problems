"""
MaxContigSumArray

Given an array of integers (negative and positive), return the 
max sum of contiguous elements in array. Write iterative
and recursive solutions.

Cases
1) Empty array
2) 1 element
3) Positive and negative integers
4) All negative integers (max sum is smallest negative integer)
5) Max sum includes sequence of negative integers in between large positive integers
7) Max sum equals one large positive integer

Approach
1) Loop through array keep track of cur_pos, cur_sum
2) Stopping condition? i < len(arr1)-1, return max_sum
3) If cur_sum > max_sum, update max_sum
4) CHECK, if cur_sum + arr[cur_pos+1] < 0, RESET (cur_pos+=1, cur_sum=arr[cur_pos+1])
5) CHECK, if arr[cur_pos+1] > (arr[cur_pos+1] + cur_sum), RESET (cur_pos+=1, cur_sum=arr[cur_pos+1])
6) ELSE, cur_sum+= arr[cur_pos+1], cur_pos+=1

Three cases:
1) adding the next value to cur sum brings cur_sum below zero, then we reset
2) the next value is greater than the combined sum, then we reset
3) the combined sum is greater, so we combine and continue

max=1
cur=3
i      S
1,2,-4,6 (while i<3)
"""

def max_contig_sum_iter(arr1):
	max_sum = arr1[0]
	cur_sum = arr1[0]
	for i in range(len(arr1)):
		if cur_sum > max_sum:
			max_sum = cur_sum
		if i == len(arr1)-1:
			return max_sum
		elif cur_sum + arr1[i+1] < 0:
			cur_sum = arr1[i+1]
		elif cur_sum + arr1[i+1] < arr1[i+1]:
			cur_sum = arr1[i+1]
		else:
			cur_sum += arr1[i+1]
	return max_sum

def max_contig_sum_recur(arr1):
	pass


# Tests
a1 = [1,5,2,5]
a2 = [1,-4,6]
a3 = [-3,-1,-7,-3]
a4 = [6]

def test_max_contig_sum_iter():
	assert max_contig_sum_iter(a1) == 13
	assert max_contig_sum_iter(a2) == 6
	assert max_contig_sum_iter(a3) == -1
	assert max_contig_sum_iter(a4) == 6 

def test_max_contig_sum_recur():
	assert max_contig_sum_recur(a1) == 13
	assert max_contig_sum_recur(a2) == 6
	assert max_contig_sum_recur(a3) == -1
	assert max_contig_sum_recur(a4) == 6 


if __name__ == "__main__":
	test_max_contig_sum_iter()
	test_max_contig_sum_recur()