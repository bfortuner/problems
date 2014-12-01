def all_chars_in(list1, val):
    for e in str(val):
        if int(e) not in list1:
             return False
    return True
             
def num_in_order(num):
    prior = str(num)[0]
    for i in range(1,len(str(num))):
        cur = str(num)[i]
        if int(cur) < int(prior):
            return False
        prior = cur
    return True

def all_num_unique(num):
    list1 = []
    for n in str(num):
        if n in list1:
            return False
        else:
            list1.append(n)
    return True

def pset_m(l1, m):
    num = int(str(9)*m)
    startlist = [x for x in range(num) if len(str(x)) == m]
    pset = []
    for k in startlist:
        if all_chars_in(l1,k) and num_in_order(k) and all_num_unique(k):
            pset.append([k])
    return pset

def powerset(l1):
    pset = []
    i = 1
    while i <= len(l1):
        pset = pset + pset_m(l1,i)
        i += 1
    return pset



print powerset([1,2,3,4,5])


