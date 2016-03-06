
#Cases
"""
One or Both Equal None (False)
Both Empty strings (True)
Only One Empty (False)
Anagrams
  All distinct letters
  Some duplicates
Not Anagrams
  ditto..

*Only Alpha-numeric allowed?
*How about whitespace? Let's assume that is a character
*How about capitalization?
"""

#Approaches
"""
1) Sort Strings and verify they are equal
2) Use HashMap to store count of each letter (can get fancy with add/remove entries)
3) Create hash function that is based solely on ASCII int value of strings, if the values are equal than strings are the same?
"""


def prevalidate_anagram(str1, str2):
	if str1 is None or str2 is None:
		return False
	if str1 == str2:
		return True
	str1_len = len(str1)
	str2_len = len(str2)
	if str1_len == 0 and str2_len == 0:
		return True
	if str1_len != str2_len:
		return False
	return None

def sort_helper(str1):
	sorted_str = "".join(sorted(str1)) #returns list
	return sorted_str

def is_anagram_sorting(str1, str2):
	str1 = sort_helper(str1)
	str2 = sort_helper(str2)
	return str1 == str2

def is_anagram_hashmap(str1, str2):
	countmap = {}
	for s in str1:
		if countmap.get(s):
			countmap[s] += 1
		else:
			countmap[s] = 1

	for s in str2:
		if countmap.get(s) is None:
			return False
		elif countmap.get(s) == 1:
			del countmap[s]
		else:
			countmap[s] -= 1
	return True

def is_anagram_hash_func(str1, str2):
	#Assume only allowed values are A ,B,C,D, so primes are [2,3,5,7]
	#verfifies strings are same length
	#http://stackoverflow.com/questions/18781106/generate-same-unique-hash-code-for-all-anagrams
	prevalid = prevalidate_anagram(str1, str2) 
	if prevalid is not None:
		return prevalid
	primes_map = {"A":2, "B":3, "C":5, "D":7}
	str1_sum = 0
	str2_sum = 0
	i = 0
	while i < len(str1):
		str1_sum += ord(str1[i]) * primes_map[str1[i]]
		str2_sum += ord(str2[i]) * primes_map[str2[i]]
		i+=1
	return str1_sum == str2_sum




# Tests

def test_prevalidate_anagram():
	assert prevalidate_anagram(None,None) == False
	assert prevalidate_anagram(" ",None) == False
	assert prevalidate_anagram("A","A") == True
	assert prevalidate_anagram("","") == True
	assert prevalidate_anagram("A","AA") == False
	assert prevalidate_anagram("ABC","AAA") == None

def test_sort_helper():
	assert sort_helper("BCA") == "ABC"
	assert sort_helper("AB ") == " AB"

def test_is_anagram_sorting():
	assert is_anagram_sorting("BCA","CAB") == True
	assert is_anagram_sorting("BCA","CAA") == False
	assert is_anagram_sorting("abA","baa") == False

def test_is_anagram_hashmap():
	assert is_anagram_hashmap("BCA","CAB") == True
	assert is_anagram_hashmap("BCA","CAA") == False
	assert is_anagram_hashmap("abA","baa") == False
	assert is_anagram_hashmap("abAAWD","baaCD") == False
	assert is_anagram_hashmap("ab AB "," Ba bA") == True
	assert is_anagram_hashmap(" "," ") == True

def test_is_anagram_hash_func():
	assert is_anagram_hash_func("BCA","CAB") == True
	assert is_anagram_hash_func("BCA","CAA") == False


if __name__ == "__main__":
	test_prevalidate_anagram()
	test_sort_helper()
	test_is_anagram_sorting()
	test_is_anagram_hashmap()
	test_is_anagram_hash_func()