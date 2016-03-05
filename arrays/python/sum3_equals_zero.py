
def sum3_equals_zero_naive(arr):
	#[1,2,3]
	"""
	Given array of integers, return true if 
	any 3 elements in array sum to zero
	"""
	if arr is None or len(arr) < 3:
		return False
	#3 loops
	i = 0
	while i < len(arr)-2:
		j = i+1
		while j < len(arr)-1:
			k = j+1
			while k < len(arr):
				sum_arr = arr[i] + arr[j] + arr[k]
				if sum_arr == 0:
					return True
				k+=1
			j+=1
		i+=1
	return False

def test_sum3_equals_zero_naive():
	a1 = [] #False
	a2 = [1] #False
	a3 = [1,2] #False
	a4 = [1,2,3] #False
	a5 = [-1,0,1] #True
	a6 = [-5,3,-1,99,0] #False
	a7 = [-1,0,1,-5,5] #True

	assert sum3_equals_zero_naive(a1) == False
	assert sum3_equals_zero_naive(a2) == False
	assert sum3_equals_zero_naive(a3) == False
	assert sum3_equals_zero_naive(a4) == False	
	assert sum3_equals_zero_naive(a5) == True
	assert sum3_equals_zero_naive(a6) == False
	assert sum3_equals_zero_naive(a7) == True

if __name__ == "__main__":
	test_sum3_equals_zero_naive()