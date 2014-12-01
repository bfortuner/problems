## Given set, return power set



def starting_dict(m):
    dic = {}
    for i in range(m):
        dic[i] = 0
    return dic

def powerset_1(set1, m):
    powerset = []
    i = 0
    while i < len(set1):
        powerset.append([set1[i]])
        i += 1
    return powerset


def powerset_2(set1, m):
    powerset = []
    i = 0
    while i < len(set1):
        j = i + 1
        while j < len(set1):
            powerset.append([set1[i],set1[j]])
            j += 1
        i += 1
    return powerset


def powerset_3(set1, m):
    powerset = []
    i = 0
    while i < len(set1):
        j = i + 1
        while j < len(set1):
            k = j + 1
            while k < len(set1):
                powerset.append([set1[i],set1[j],set1[k]])
                k += 1
            j += 1
        i += 1
    return powerset



# Initial
def powerset(set1, subset, start, m):
    pset = []
    for i in range(start, len(set1)):
        subset.append(set1[i])
        if len(subset) == m:
            pset.append(subset)
            subset = subset[:-1]
        else:
            pset = pset + powerset(set1, subset, i+1, m)
            subset = subset[:start]
    return pset


# Second
def powerset1(set1, subset, start, m):
    pset = []
    for i in range(start, len(set1)):
        subset.append(set1[i])
        if len(subset) == m:
            return subset
        else:
            pset = pset + powerset(set1, subset, i+1, m)
            subset = subset[:start]
    return pset


def powerset2(set1, subset, pos, m):
    pset = []
    subset.append(set1[pos])
    if len(subset) == m:
        return subset
    else:
        pset = pset + powerset(set1, subset, pos+1, m)
        subset = subset[:pos]
    return pset





s = [1,2]
s1 = [1,2,3]
s2 = [1,2,3,4]
s3 = [1,2,3,4,5]
s4 = [1,2,3,4,5,6]
s5 = [1,2,3,4,5,6,7]
s6 = [1,2,3,4,5,6,7,8,9,10]

print powerset1(s,[],0,1)
print powerset1(s1,[],0,3)
print powerset1(s2,[],0,3)
print powerset1(s3,[],0,3)
#print powerset1(s4,[],0,3)

# Full Powerset
#print pset(s)
#print pset(s1)
#print pset(s2)
#print pset(s3)
#print powerset1(s3,[],0,4)
#print pset(s4)
#print pset(s5)
#print pset(s6)



'''
# Powerset 1
print powerset(s, [], 0, 1)
print powerset(s1, [], 0, 1)
print powerset(s2, [], 0, 1)
print powerset(s3, [], 0, 1)
print powerset(s4, [], 0, 1)
print powerset(s5, [], 0, 1)
print powerset(s6, [], 0, 1)

# Powerset 2
print powerset(s, [], 0, 2)
print powerset(s1, [], 0, 2)
print powerset(s2, [], 0, 2)
print powerset(s3, [], 0, 2)
print powerset(s4, [], 0, 2)
print powerset(s5, [], 0, 2)
print powerset(s6, [], 0, 2)

# Powerset 3
#print powerset(s, [], 0, 3)
print powerset(s1, [], 0, 3)
print powerset(s2, [], 0, 3)
print powerset(s3, [], 0, 3)
print powerset(s4, [], 0, 3)
print powerset(s5, [], 0, 3)
print powerset(s6, [], 0, 3)

# Powerset 4
print powerset(s3, [], 0, 4)
print powerset(s4, [], 0, 4)
print powerset(s5, [], 0, 4)
print powerset(s6, [], 0, 4)
'''


def pset(set1):
    pset = []
    for i in range(len(set1)+1):
        print powerset(set1, [], 0, i)
        pset = pset + powerset(set1, [], 0, i)
    return len(set1), len(pset), 2**len(set1)

