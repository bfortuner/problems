
## CASES
"""
None
"" 
"A"
"ABC"
"ABBCA"
"""

## APPROACHES
"""
1) Sort string. Loop once. Remove next if char is same. (in place)
2) New string. HashMap. Loop once. If map contains val, don't add. (Could also use set).
3) Same string. Remove in place
"""

def remove_dupes_sort(str1):
	newstr = ""
	str1 = "".join(sorted(str1))
	i = 0
	while i < len(str1):
		newstr += str1[i]
		if i == len(str1)-1:
			return newstr
		elif str1[i] == str1[i+1]:
			while i < len(str1)-1 and str1[i] == str1[i+1]:
				i += 1
		i += 1
	return newstr 

def remove_dupes_map(str1):
	charmap = {}
	newstr = ""
	for s in str1:
		if charmap.get(s) is None:
			newstr += s
			charmap[s] = 1
	return newstr			

def remove_dupes_in_place(str1):
	if len(str1) < 2:
		return str1
	i = 0
	while i < len(str1)-1:
		print len(str1) #python keeps updating length of string
		k = i+1
		while k < len(str1):
			if str1[i] == str1[k]:
				if k == len(str1)-1:
					str1 = str1[:k]
				else:
					str1 = str1[:k] + str1[k+1:]
			else:
				k+=1
		i+=1
	return str1

#5(4)
#ABACB
#ABCB
#ABC



## Tests

def test_remove_dupes_sort():
	assert remove_dupes_sort("CABABABDCC") == "ABCD"
	assert remove_dupes_sort("ABC") == "ABC"
	assert remove_dupes_sort("") == ""

def test_remove_dupes_map():
	assert remove_dupes_map("CABABABDCC") == "CABD"
	assert remove_dupes_map("ABC") == "ABC"
	assert remove_dupes_map("") == ""

def test_remove_dupes_in_place():
	assert remove_dupes_in_place("CABABABDCC") == "CABD"
	assert remove_dupes_in_place("ABC") == "ABC"
	assert remove_dupes_in_place("") == ""

if __name__ == "__main__":
	test_remove_dupes_sort()
	test_remove_dupes_map()
	test_remove_dupes_in_place()

