import math

class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        if A <= 2:
            return []
        prime = 2
        while not self.is_prime(A - prime):
            prime = self.get_next_prime(prime)
        return [prime, A-prime]
        
    def get_next_prime(self, n):
        i = n + 1
        while True:
            if self.is_prime(i):
                return i
            i+=1
    
    def is_prime(self, n):
        if n < 2:
            return False
        i = 2
        while i <= int(math.sqrt(n)):
            if n % i == 0:
                return False
            i+=1
        return True


sol = Solution()

print sol.primesum(34) == [3,31]
print sol.primesum(4) == [2,2]