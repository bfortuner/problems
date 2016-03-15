"""
Longest Substring No Dupes
Given a string, please get the length of the longest substring 
which does not have duplicated characters. 
Supposing all characters in the string are in the range from 'a' to 'z'. 
Input: "ababc", Output: 3.
"""

#Cases
"""
1) Empty or None
2) Single char
3) Normal string (whole is unique)
4) Normal string (part is unique - beginning/end)
"""

#Approaches
"""
1) Store cur_length, max_length, cur_index, setofchars. Loop through O(n^2) use set to 
know dupes. Keep track of longest substring without dupes. Reset if dupe found.
"""

def get_len_longest_substr(str1):
	#hashmap which stores unique chars in string
	#Once dupe is found, we clear hashmap and start again
	cur_substr_chars = set()
	max_length = 0
	start_index = 0
	i = 0
	while i < len(str1):
		if str1[i] not in cur_substr_chars:
			cur_substr_chars.add(str1[i])
			if i-start_index+1 > max_length:
				max_length = i-start_index+1
			i += 1
		else:
			cur_substr_chars = set()
			start_index += 1
			i = start_index
	return max_length


#Tests

def test_get_len_longest_substr():
	assert get_len_longest_substr("abcadd") == 4
	assert get_len_longest_substr("abcabc") == 3
	assert get_len_longest_substr("aaa") == 1
	assert get_len_longest_substr("abcad") == 4
	assert get_len_longest_substr("a") == 1
	assert get_len_longest_substr("") == 0
	assert get_len_longest_substr("abc") == 3

if __name__ == "__main__":
	test_get_len_longest_substr()

