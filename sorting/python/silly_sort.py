def sort(arr):
	for i in range(len(arr)):
		arr = silly(arr,arr[i])
	return arr

def silly(buckets, num):
	if buckets[num] == num:
		return buckets
	tmp = buckets[num]
	buckets[num] = num
	return silly(buckets, tmp)


print sort([2,1,0])
print sort([3,1,4,2,5,0])

