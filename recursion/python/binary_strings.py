#3

def generate_binary_str(n, curstr):
    if len(curstr) > n:
        return []
    if len(curstr) > 1 and curstr[0] == "0":
        return []
    strings = []
    if curstr != "":
        strings.append(curstr)
    return strings + generate_binary_str(n, curstr + "1") + \
        generate_binary_str(n, curstr + "0")

def generate_binary_str2(n):
    if n == 0:
        return []
    if n == 1:
        return ["1","0"]
    longer = []
    smaller = generate_binary_str2(n-1)
    for s in smaller:
        if len(s) == n-1 and s[0] != "0":
            longer.append(s + "1")
            longer.append(s + "0")
    return longer + smaller

def appendAtFront(x, arr):
    return [x + element for element in arr]

def bitString(n):
    if n == 0:
        return []
    if n == 1:
        return ["0","1"]
    return appendAtFront("0",bitString(n-1)) + \
        appendAtFront("1",bitString(n-1))

print generate_binary_str(3,"")
print generate_binary_str(4,"")

print "generating binary str 2--------"
print generate_binary_str2(1)
print generate_binary_str2(2)
print generate_binary_str2(3)
print generate_binary_str2(4)

print "generating binary str 3--------"
print bitString(1)
print bitString(2)
print bitString(3)
print bitString(4)
