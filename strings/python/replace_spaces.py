#Cases
"""
1) Empty string
2) No spaces
3) Normal some spaces
4) Multiples contiguous spaces
"""

def replace_spaces(str1):
	html_space = "%20"
	newstr = ""
	for s in str1:
		if s == " ":
			newstr += html_space
		else:
			newstr += s
	return newstr

def replace_spaces_pythonic(str1):
	#returns new copy of str 
	return str1.replace(" ", "%20")

#Tests

def test_replace_spaces():
	assert replace_spaces("") == ""
	assert replace_spaces("ABC") == "ABC"
	assert replace_spaces("A AB B") == "A%20AB%20B"
	assert replace_spaces("A  A A   AAA") == "A%20%20A%20A%20%20%20AAA"

def test_replace_spaces_pythonic():
	assert replace_spaces_pythonic("") == ""
	assert replace_spaces_pythonic("ABC") == "ABC"
	assert replace_spaces_pythonic("A AB B") == "A%20AB%20B"
	assert replace_spaces_pythonic("A  A A   AAA") == "A%20%20A%20A%20%20%20AAA"

if __name__ == "__main__":
	test_replace_spaces()
	test_replace_spaces_pythonic()