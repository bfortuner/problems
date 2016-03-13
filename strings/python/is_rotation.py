#Cases
"""
1) Empty string
2) Normal is rotation 1-step
3) Normal is rotation multistep
4) Normal no rotation same chars
5) 1,2,3+ length
6) Strings not same length == False
"""

#Approaches
"""
1) Submethod called "rotate" which rotates string one-place, main method rotates str2 len(str1) times, checks if strings are equal
2) Loop through str1 one time, if str2[i] == str1[i] then increment both and keep going. If you reach a str2[i] that doesn't 
match str1[i], you start from beginning, where str1[i] == str2[i+1]. If you reach end of str1 with all equal, return True
"""

def rotate_string(str1):
	#rotate 1 place
	if len(str1) < 2:
		return str1
	return str1[-1] + str1[:-1]

def is_rotation(str1, str2):
	if len(str1) != len(str2):
		return False
	if len(str1) == 0:
		return True
	i = 0
	while i < len(str1):
		if str1 == str2:
			return True
		str2 = rotate_string(str2)
		i+=1
	return False

def is_rotation_loops(str1, str2):
	if len(str1) != len(str2):
		return False
	if len(str1) == 0:
		return True
	attempts = len(str1)
	str1_pos = 0
	str2_pos = 0
	str2_start = 0
	are_rotations = True
	while attempts > 0 and str1_pos < len(str1):
		are_rotations = True
		if str2_pos == len(str1):
			str2_pos = 0
		if str1[str1_pos] != str2[str2_pos]:
			are_rotations = False
			str2_start += 1
			str2_pos = str2_start
			str1_pos = 0
			attempts -= 1
		else:
			str1_pos += 1
			str2_pos += 1
	return are_rotations




#Tests

def test_rotate_string():
	assert rotate_string("ABC") == "CAB"
	assert rotate_string("BA") == "AB"
	assert rotate_string("") == ""
	assert rotate_string("A") == "A"

def test_is_rotation():
	assert is_rotation("ABC","CAB") == True
	assert is_rotation("ABC","BCA") == True
	assert is_rotation("","") == True
	assert is_rotation("AABB", "ABAB") == False
	assert is_rotation("A","A") == True

def test_is_rotation_loops():
	assert is_rotation_loops("ABC","CAB") == True
	assert is_rotation_loops("ABC","BCA") == True
	assert is_rotation_loops("","") == True
	assert is_rotation_loops("AABB", "ABAB") == False
	assert is_rotation_loops("A","A") == True

if __name__ == "__main__":
	test_rotate_string()
	test_is_rotation()
	test_is_rotation_loops()

