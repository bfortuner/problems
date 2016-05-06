import math

def column_title_to_num(A):
    L="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    total = 0
    exponent = len(A)-1
    for char in A:
        decimal = L.find(char)+1 #ord(char)-ord("A")+1
        total += (decimal * math.pow(26,exponent))
        exponent-=1
    return int(total)

print column_title_to_num("A") == 1
print column_title_to_num("Z") == 26
print column_title_to_num("AA") == 27
print column_title_to_num("AB") == 28
print column_title_to_num("ZZZZZ")