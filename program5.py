'''
list=[1,4,6,3,7]
large=max(list)
largest=list[0]
for num in list:
    if num>largest:
        largest=num
print(largest)
print(large)
'''
'''
list=[1,4,6,3,7]
large=min(list)
smallest=list[0]
for num in list:
    if num<smallest:
        smallest=num
print(smallest)
print(large)
'''
'''
list=[2,4,3,5,1,7]
list.sort()
print(list[-2])'''
'''
li=int(map(int,input("given No is:".split)))
newli=li[::-1]
print(newli)
'''
'''nums=[0,1,2,3,0,0,3]
count=0
while 0 in nums:
    nums.remove(0)
    count+=1

while count>0:
    nums.append(0)
    count-=1
print(nums)'''
'''
height=[1,8,6,2,5,4,8,3,7]
n=len(height)
areas=[]
for i in range(n):
    for j in range(i+1,n):
        area= min(height[i], height[j]) * (j - i)
        areas.append(area)
print(max(areas))
'''
'''
height=[8,7,2,1]
n=len(height)
left=0
right=n-1
max_area=0
while left<right:
    width=right-left
    area=min(height[left],height[right])*width
    max_area=max(max_area,area)
    if height[left]<height[right]:
            left+=1
    else:
            right-=1 
print(max_area)   
'''
'''
from typing import List
nums=[6,5,5]
n = len(nums)
for i in range(n):
    cnt = 0
    for j in range(n):
        if nums[j] == numscnt += 1:
             cnt += 1          
        if cnt > (n // 2):        
            print(nums[i])
            break
'''
'''
s="hi i am supriya"
lst=s.split()
length=len(lst[-1])
print(length)'''\

s = "A man, a plan, a canal: Panama"
s.replace(","," ")
pall=s[::-1]
print(pall)
if pall==s:
    print(True)
else:
    print(False)    






