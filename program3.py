'''
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))
'''
class Solution(object):
    def reverse(self, x):
       self.x=x
       new_num=0
       if x>0:
           while x>0:
                digit=x%10
                new_num=new_num*10+digit
                x=x/10
           return new_num
       elif x<0:
            while x<0:
                digit=x%10
                new_num=(-new_num*10+digit)
                x=x/10
            return new_num
