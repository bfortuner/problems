"""
Longest Substring No Dupes
Given a string, please get the length of the longest substring 
which does not have duplicated characters. 
Supposing all characters in the string are in the range from ‘a’ to ‘z’. 
Input: "ababc", Output: 3.
"""

#Cases
"""
1) Empty or None 
3) Single word
4) Periods and special characters?
5) Normal sentence w spaces as delimeter
"""

#Approaches
"""
1) Split string into Array delimited by space. Create new string. 
Loop through array backwards and append to new string delimited by space.
2) New String. Loop through Original String until first space found. Keep track
of index and append substring every time space is found.
"""

def reverse_sentence_array(str1):
	if str1 == "" or str1 == None:
		return ""
	sentence_array = str1.split(" ")
	i = len(sentence_array)-1
	reversed_sentence = ""
	while i >= 0:
		if sentence_array[i] != "":
			reversed_sentence += sentence_array[i] + " "
		i -= 1
	return reversed_sentence.rstrip()


#Tests

s1 = "I am a student"
s2 = ""
s3 = "AAA"
s4 = " AAA "
s5 = "BB     BB"

a1 = "student a am I"
a2 = ""
a3 = "AAA"
a4 = "AAA"
a5 = "BB BB"


def test_reverse_sentence_array():
	assert reverse_sentence_array(s1) == a1
	assert reverse_sentence_array(s2) == a2
	assert reverse_sentence_array(s3) == a3
	assert reverse_sentence_array(s4) == a4
	assert reverse_sentence_array(s5) == a5

if __name__ == "__main__":
	test_reverse_sentence_array()

