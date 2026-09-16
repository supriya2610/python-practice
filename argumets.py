def multi(*args):
    print(args)
a=multi(1,3,4,5,5,7)
print(a) 

def add(x,y):
    return x+y
nums=[1,5]
print(add(*nums))#  here if we dont give * then x will take list[1,5] y wiill not take 
print(add(nums))

#kwargs keyword argyments
def greet(**kwargs):
    print(kwargs)
return(ame="supray",age=23))
