letters = {
	"1":"a",
	"2":"b",
	"3":"c",
	"11":"d",
	"12":"e",
	"23":"f",
	"1123":"g"
	}

"""
input: "1123"
output: ["aabc","aaf","aec","dbc","df","g"]	
"""

def interpret(symbols, curstr, start, end):
	if end > len(symbols):
		return []
	seq = symbols[start:end]
	if seq in letters:
		newstr = curstr + letters[seq]
		if end == len(symbols):
			return [newstr]
		return interpret(symbols, newstr, end, end+1) + \
		interpret(symbols, curstr, start, end+1)
	else:
		return interpret(symbols, curstr, start, end+1)

print interpret("1123","",0,1)
print interpret("1","",0,1)
print interpret("23","",0,1)

