'''powerset for any symbol'''

def subsets_m(set, m, pos):
    p = []
    while m > 0 and pos <= len(set)-m:
        subs = subsets_m(set, m-1, pos+1)
        for s in subs:
            p.append([set[pos]] + s)
        pos += 1
    if p == []:
        return [[]]
    return p

def pset(set):
    p = [[]]
    m = 1
    while m <= len(set):
        p = p + subsets_m(set,m,0)
        m += 1
    return p

# Test cases                                                                                                                                                                                  
print len(pset(['a']))
print len(pset(['a','b']))
print len(pset(['a','b','c']))
print len(pset(['a','b','c','d']))
print len(pset(['a','b','c','d','e']))
print len(pset(['a','b','c','d','e','f']))
print len(pset(['a','b','c','d','e','f','g']))
print len(pset(['a','b','c','d','e','f','g','h']))
