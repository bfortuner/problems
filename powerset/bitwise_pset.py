def pset_binary(n, m):
    '''Generate Powerset Using Binary Digits'''
    k = 1
    last_k = 0
    subsets = []
    i = n
    bin_array = [0 for x in range(n)]
    while i > 0:
        if bin_array[i-1] == 0:
            bin_array[i-1] = 1
            subsets.append(bin_array[:])
            if sum(bin_array) == m:
                last_k = k
            i = n
            k+=1
        else:
            bin_array[i-1] = 0
            i -= 1
    return subsets

#####################################################

def bin_str_to_int(x):
    return int(x, 2)

def int_to_bin_str(x):
    return format(x, '#010b')[2:]

def left_shift(x, y):
    '''
    Shift x to the left, y places
    equals x * (2**y)
    '''
    x = bin_str_to_int(x)
    y = bin_str_to_int(y)    
    return int_to_bin_str(x << y)

def right_shift(x, y):
    '''
    Shift x to the right, y places
    equals x // (2**y)
    '''
    x = bin_str_to_int(x)
    y = bin_str_to_int(y)
    return int_to_bin_str(x >> y)

def bxor(x, y):
    x = bin_str_to_int(x)
    y = bin_str_to_int(y)
    return int_to_bin_str(x ^ y)

def band(x, y):
    x = bin_str_to_int(x)
    y = bin_str_to_int(y)
    return int_to_bin_str(x ^ y)

def bor(x, y):
    x = bin_str_to_int(x)
    y = bin_str_to_int(y)
    return int_to_bin_str(x ^ y)

def is_set(x, i):
    '''
    x binary str
    Return true if element at position i
    in binary string, x, is 1

    ex: i is set!
    0000 1111 |
    0000 0100
    =========
    0000 1111 == 0000 1111

    ex: i is not set!
    0000 1011 |
    0000 0100
    =========
    0000 1111 != 0000 1011 
    '''
    x = bin_str_to_int(x)
    z = x | 1<<i
    return x == z

    # Alternative solution
    #return int_to_bin_str((x & 1<<i) > 0)

def set_to_1(x, i):
    '''
    x binary str
    Set element at position i
    in binary string to 1

    e.g. set_in_use('1000 0000', 3)
    1000 0000 |
    0000 1000
    =========
    1000 1000
    '''
    x = bin_str_to_int(x)
    return int_to_bin_str(x | 1<<i)

def set_to_0(x, i):
    '''
    x binary str
    Set element at position i
    in binary string to 0

    e.g. set_to_0('1000 0000', 2)
    1000 0100 & 
    1111 1011
    =========
    1000 0000 ^ 00000000
    '''
    if is_set(x,i):
        x = bin_str_to_int(x)
        return int_to_bin_str(1<<i ^ x)
    else:
        return x


def hacking_around(n, m):
    '''
    #n=8,m=2

    0000 0011 ^ 0000 0110
    0000 0101 ^ 0000 0011
    0000 0110 ^ 0000 1111
    0000 1001 ^ 0000 0011
    0000 1010 ^ 0000 0110
    0000 1100 ^ 0001 1101
    0001 0001
    0001 0010
    '''
    x = n**m - 1
    while x < n**(m+1):
        print int_to_bin_str(x)
        x+=1
    return x


def pset2(n, m):
    pset = [] 
    i = 1
    val = 2**m-1    
    while i < n:
        print int_to_bin_str(val)
        k = 0
        while k < i-1:
            val = val ^ (1<<k+1 | 1<<k)
            print int_to_bin_str(val)
            k+=1
        val = val ^ (1<<i+1 | 1<<i)
        i+=1
    return pset

def pset_recursive(n, m, val):
    pset = [] 
    if m == 0:
        return res
    i = 1
    while i < n:
        val = val ^ (1<<i+1 | 1<<i)
        pset.append(int_to_bin_str(val))
        pset = pset + pset_recursive(n,m-1,val)
        i+=1
    val = val & 0 | (1<<i+1 | 1<<0)
    pset.append(val)
    return pset


print "testing is_set ---------"
print is_set('00001111',2) == True
print is_set('00001011',2) == False
print is_set('00000000',2) == False
print is_set('11111111',2) == True

print "testing set_to_1 ---------"
print set_to_1('00001000', 2) == '00001100'
print set_to_1('11111111', 2) == '11111111'
print set_to_1('00000000', 2) == '00000100'

print "testing set_to_0 ---------"
print set_to_0('00001111', 2) == '00001011'
print set_to_0('00001011', 2) == '00001011'
print set_to_0('11111111', 2) == '11111011'

print "generating sample powerset n,m ---------"

n=8
m=2

sets = pset2(n,m)
#sets = pset_recursive(n,m,0)
'''
sets = pset_binary(n,m)
for s in sets:
    if sum(s) == m:
        bin_str = str(s).replace(', ','').replace('[','').replace(']','')
        val = bin_str_to_int(bin_str)
        jump = val-last_val
        last_val = val
        print bin_str #, jump
'''
