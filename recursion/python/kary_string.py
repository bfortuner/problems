"""
Generate all the strings of length n with k character options
e.g. How many unique codes can I generate with of length N with K letters?
examples: Amazon vendor codes. KEHAE or ASINs, B00AEB3FE
k^n
input: (2, ["ABC"])
output = ["AA","AB","AC","BA","BB","BC","CA","CB,"CC"]
"""

def appendChar(c, arr):
    return [elem + c for elem in arr]

def kary_str(n, chars):
    if n == 0:
        return []
    if n == 1:
        return chars
    strs = []
    for c in chars:
        strs += appendChar(c, kary_str(n-1,chars))
    return strs


print kary_str(2,["A","B","C"])
    
