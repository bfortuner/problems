"""
[FindFirstUniqueChar]
Return the first non-repeated character in a string. 
If not found, return null. Assume the string is NOT sorted. 
"""

#Cases
"""
1) Empty or None 
2) No repeats
3) Single repeat 
4) Multiple repeats (return first found?)
5) 1,2,3 length strings
"""

#Approaches
"""
1) Sort string O(n log n), then loop O(n) and check if str1[i] == str1[i+1] (Won't work for first unique)
2) HashMap to store unique chars. Loop O(n) check if in HashMap, if not, store.
3) Naive Double Loop O(n^2), For each, for each, see if another exists. Return first found.
4) Can we do linear time?
"""

def get_first_unique_char_loops(str1):
	i = 0
	while i < len(str1):
		j = i+1
		while j < len(str1):
			if str1[i] == str1[j]:
				return str1[i]
			j+=1
		i+=1
	return None

def get_first_unique_char_dict(str1):
	chars = {}
	for s in str1:
		if chars.get(s) != None:
			return s
		chars[s] = s
	return None


#Tests

def test_get_first_unique_char_loops():
	assert get_first_unique_char_loops("ABCBD") == "B"
	assert get_first_unique_char_loops("") == None
	assert get_first_unique_char_loops("A") == None
	assert get_first_unique_char_loops("AB") == None
	assert get_first_unique_char_loops("ABCC") == "C"

def test_get_first_unique_char_dict():
	assert get_first_unique_char_dict("ABCBD") == "B"
	assert get_first_unique_char_dict("") == None
	assert get_first_unique_char_dict("A") == None
	assert get_first_unique_char_dict("AB") == None
	assert get_first_unique_char_dict("ABCC") == "C"

if __name__ == "__main__":
	test_get_first_unique_char_loops()
	test_get_first_unique_char_dict()


