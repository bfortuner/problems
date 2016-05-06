import math

def gcd(A, B):
    if A == 0:
        return B
    if B == 0:
        return A
    max_found = 1
    if A < B:
        small = A
        large = B
    else:
        small = B
        large = A
    stop = int(math.sqrt(small))
    i = 1
    while i <= stop:
        sf = i
        lf = small/i
        if small % lf == 0 and large % lf == 0:
            return lf
        if small % sf == 0 and large % sf == 0:
            if sf > max_found:
                max_found = sf
        i+=1
    return max_found



"""
Euclid's GCD 
-------------
gcd(16,12)
  16 % 12 == 4
  gcd(12,4)
    12 % 4 == 0
    gcd(4,0)
    return small == 4
"""
def gcd_euclids(large, small):
    if small == 0:
        return large
    return gcd(small, large % small)


print "gcd_better-----"
print gcd_euclids(12,15)
print gcd_euclids(9,3)
print gcd_euclids(9,6)
print gcd_euclids(16,12)
print gcd_euclids(16,8)
print gcd_euclids(16,16)
print gcd_euclids(16,1)
print gcd_euclids(16,0)
print gcd_euclids(7,5)

print "gcd--------"
print gcd(16,12)
print gcd(16,8)
print gcd(16,16)
print gcd(16,1)
print gcd(16,0)
print gcd(7,5)