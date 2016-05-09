"""
Return all purmutations of str1

ABC = ['ABC', 'BAC', 'BCA', 'ACB', 'CAB', 'CBA']
Permutations = N!
Combinations = N^2
Combinations size M = N!/M!(N-M)!

"""
def permutate(str1, curstr):
	if len(str1) <= 1:
		return [curstr + str1]
	permutations = []
	for i in range(1,len(str1)):
		permutations += permutate(str1[1:i]+str1[i+1:], curstr+str1[0]+str1[i])
		permutations += permutate(str1[:i]+str1[i+1:], curstr+str1[i])
	return permutations


print permutate("ABC","")
print len(permutate("ABCD",""))