import sys
from math import sqrt, log


def builder(m):
    if m <= 0:
        return ""
    else:
        return str(m) + " " + builder(m-1)


print builder(4)
print builder(5)
print builder(6)

def tester(n, m):
    res = []
    i_build = builder(m-2)
    i = 0
    while i <= (n-m):
        res.append(str(i) + " " + i_build)
        k = 0
        k_build = builder(i-1)
        while k <= i:
            j = 0
            res.append(str(k) + " " + k_build)
            while j <= k:
                res.append(str(j)) #+ " " + builder(0)
                j+=1
            k+=1
        i+=1
    return res


#args = sys.argv
#res = tester(int(args[1]), int(args[2]))
#for val in res:
#    print val


def get_odd_calc(num):
    dict = {}
    dict[1] = '0'
    dict[2] = '1'
    dict[3] = '1 + 0'
    dict[4] = '2'
    dict[5] = '2 + 0'
    dict[7] = '2 + 1 + 0'
    dict[8] = '3'
    dict[9] = '3 + 0'
    dict[11] = '3 + 1 + 0'
    dict[15] = '3 + 2 + 1 + 0'
    dict[16] = '4'
    dict[17] = '4 + 0'
    dict[19] = '4 + 1 + 0'
    dict[23] = '4 + 2 + 1 + 0'
    dict[31] = '4 + 3 + 2 + 1 + 0'
    dict[32] = '5'
    dict[33] = '5 + 0'
    dict[35] = '5 + 1 + 0'
    dict[39] = '5 + 2 + 1 + 0'
    dict[47] = '5 + 3 + 2 + 1 + 0'
    dict[63] = '5 + 4 + 3 + 2 + 1 + 0'
    dict[64] = '6'
    dict[65] = '6 + 0'
    dict[67] = '6 + 1 + 0'
    dict[71] = '6 + 2 + 1 + 0'
    dict[79] = '6 + 3 + 2 + 1 + 0'
    dict[95] = '6 + 4 + 3 + 2 + 1 + 0'
    dict[127] = '6 + 5 + 4 + 3 + 2 + 1 + 0'
    dict[128] = '7'
    dict[129] = '7 + 0'
    dict[131] = '7 + 1 + 0'
    dict[135] = '7 + 2 + 1 + 0'
    dict[143] = '7 + 3 + 2 + 1 + 0'
    dict[159] = '7 + 4 + 3 + 2 + 1 + 0'
    dict[191] = '7 + 5 + 4 + 3 + 2 + 1 + 0'
    dict[255] = '7 + 6 + 5 + 4 + 3 + 2 + 1 + 0'
    dict[256] = '8'
    dict[257] = '8 + 0'
    dict[259] = '8 + 1 + 0'
    dict[263] = '8 + 2 + 1 + 0'
    dict[271] = '8 + 3 + 2 + 1 + 0'
    dict[287] = '8 + 4 + 3 + 2 + 1 + 0'
    dict[319] = '8 + 5 + 4 + 3 + 2 + 1 + 0'
    dict[383] = '8 + 6 + 5 + 4 + 3 + 2 + 1 + 0'
    dict[511] = '8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 + 0'
    try:
        return dict[num]
    except:
        return log(num, 2)

# Generate Powerset Using Binary Digits
def pset_binary(n, m):
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
                print_num = get_odd_calc(k-last_k)
                #print print_num
                print bin_array, k, " ----- ", print_num  #bin(k-last_k)[2:]
                last_k = k
            i = n
            k+=1
        else:
            bin_array[i-1] = 0
            i -= 1
    return subsets



#pset_binary(int(args[1]), int(args[2]))

#pset_binary(10, 3)
#pset_binary(8, 4)
#pset_binary(10, 5)


def gen_2_set(n, m):
    i = 0
    sum = 2**m-1
    while i <= (n-m):
        exp = 0
        while exp < i:
           sum += 2**exp
           print sum, exp, 2**exp
           exp+=1
        sum += (2**(exp)+1)
        print sum, exp+1, (2**(exp)+1)
        i+=1
    return sum


#gen_2_set(10, 2)
