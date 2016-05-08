#A == Integer
#Get all primes up to A
#interviewbit.com/problems/prime-numbers/
def sieve(A):
    primes = []
    nums = [n for n in range(A+1)]
    for i in range(2, len(nums)):
        if nums[i] is not None:
            primes.append(nums[i])
            set_multiples_to_none(nums[i], nums)
    return primes
    
def set_multiples_to_none(n, nums):
    i=2
    while n*i < len(nums):
        nums[n*i] = None
        i+=1


print sieve(10) == [2,3,5,7]