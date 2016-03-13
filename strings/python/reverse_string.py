#Cases
"""
1) Empty string
2) Normal all-distinct
3) Normal some dupes
4) even/odd number??
5) 1,2,3+ length

"""

def reverse_string(str1):
	newstr = ""
	i = len(str1)-1
	while i >= 0:
		newstr += str1[i]
		i-=1
	return newstr

def reverse_string_in_place(str1):
	#ABC / 3,0
	#CAB / 3,1
	#CBA / 3,2
	#CBA / 3,3
	i = 0
	while i < len(str1):
		str1 = str1[0:i] + str1[-1] + str1[i:-1]
		i+=1
	return str1


#Tests

def test_reverse_string():
	assert reverse_string("ABC") == "CBA"
	assert reverse_string("") == ""
	assert reverse_string("AABB") == "BBAA"
	assert reverse_string("A") == "A"

def test_reverse_string_in_place():
	assert reverse_string_in_place("ABC") == "CBA"
	assert reverse_string_in_place("") == ""
	assert reverse_string_in_place("AABB") == "BBAA"
	assert reverse_string_in_place("A") == "A"

if __name__ == "__main__":
	test_reverse_string()
 	test_reverse_string_in_place()
