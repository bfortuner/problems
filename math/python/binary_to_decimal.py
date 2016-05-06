import math
"""
IN: integer representing binary number
OUT: integer representing deimal number
"""
def binary_to_decimal(binary):
	decimal = 0
	exponent = 0
	while binary > 0:
		last_digit = binary % 10
		decimal += (last_digit * math.pow(2,exponent))
		binary /= 10
		exponent += 1
	return int(decimal)

def decimal_to_binary(decimal):
	if decimal == 0:
		return "0"
	binary = ""
	while decimal > 0:
		digit = decimal % 2
		decimal = decimal / 2
		binary = str(digit) + binary
	return binary

print binary_to_decimal(101010)
print binary_to_decimal(1)
print binary_to_decimal(0)
print binary_to_decimal(111)

print decimal_to_binary(10)
print decimal_to_binary(0)
print decimal_to_binary(1)