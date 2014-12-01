
#Iterative Powerset

def reset_subset(subset, i):
    subset[i] += 1
    i += 1
    while i < len(subset):
        subset[i] = subset[i-1] + 1
        i+=1
    return subset

def subsets_m(n, m):
    pset = []
    subset = [x for x in range(0,m)]          # [0,3,4], 5
    skip = False
    mPos = m-1                                # last pos in subset
    while mPos >= 0:
        while subset[mPos] <= (n-(m-mPos)) and not skip:
            pset.append(subset[:])
            subset[mPos] += 1
        mPos -= 1
        if subset[mPos] < (n-(m-mPos)):
            skip = False
            subset = reset_subset(subset,mPos)
            mPos = m-1
        else:
            skip = True
    return pset

def powerset(n):
    pset = []
    m = 1
    while m <= n:
        pset = pset + subsets_m(n,m)
        m+=1
    pset += [[]]
    return pset

print powerset(5)
print len(powerset(5)) == 32
