"""
ReverseWords 
Given a sentence, return the sentence in reverse order
(e.g. "I am a student" == "student a am I")
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

def reverse_sentence_string(str1):
	if str1 == "" or str1 == None:
		return ""
	str1 = str1.strip()
	reversed_str = ""
	stop = len(str1)
	start = len(str1)-1
	while start >= 0:
		while start >= 0 and str1[start] != " ":
			start -= 1
		reversed_str += str1[start+1:stop] + " "
		while start >= 0 and str1[start] == " ":
			start -= 1
		stop = start+1
	return reversed_str.rstrip()


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

def test_reverse_sentence_string():
	assert reverse_sentence_string(s1) == a1
	assert reverse_sentence_string(s2) == a2
	assert reverse_sentence_string(s3) == a3
	assert reverse_sentence_string(s4) == a4
	assert reverse_sentence_string(s5) == a5

if __name__ == "__main__":
	test_reverse_sentence_array()
 	test_reverse_sentence_string()
