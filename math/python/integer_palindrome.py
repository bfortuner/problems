import math

class Solution:
    # @param A : integer
    # @return a boolean value ( True / False )
    def get_digit_count(self, num):
        if num == 0:
            return 1
        count = 0
        while num > 0:
            count += 1
            num /= 10
        return count

    def reverse_num(self, num):
        tens = self.get_digit_count(num)-1
        reversed_num = 0
        while num > 0:
            digit = num % 10
            reversed_num += (digit * math.pow(10,tens))
            tens -= 1
            num /= 10
        return reversed_num

    def isPalindrome(self, num):
        if num < 0:
            return False
        return self.reverse_num(num) == num

sol = Solution()
print sol.isPalindrome(12121)
print sol.isPalindrome(1)
print sol.isPalindrome(0)
print sol.isPalindrome(00)
print sol.isPalindrome(111)
print sol.isPalindrome(11)
print sol.isPalindrome(101)
#False
print sol.isPalindrome(1000021)