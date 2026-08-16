nums=[1,4,6,8,6,8,7,6] 
output=[]
target=8
for i in range(len(nums)):
    if nums[i]==target:
        output.append(i)
    else:
        print([-1,-1] )  