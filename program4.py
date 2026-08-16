class Solution(object):
    def isPalindrome(self, x):
        original = x  # store original number
        newnum = 0

        while x > 0:
            digit = x % 10
            newnum = newnum * 10 + digit
            x = x // 10

        if newnum == original:
            return True
        else:
            return False
   
sol = Solution()
print(sol.isPalindrome(121))  # True
print(sol.isPalindrome(123)) 
   
