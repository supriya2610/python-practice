x,y=1,2
t=5,7
s,r=t #this is example of destructuring #
x,*y=[1,2,3,4,5,6] #here x will be assigned 1 and y will be assigned [2,3,4,5,6] here *collects all the destructor and assign it to y

#list comprehension
list=[2,4,5,6,7]
doubleed={l*3 for l in list}
print(doubleed)

