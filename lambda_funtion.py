#lambda function is a functuion which always return we use lambda keyword and pass arguments and expression in it 
#syntax : lambda arguments :expression
lambda x,y:x+y
m= lambda x,y:x+y
print(m(2,4))
#there is one more way to call it without using a variable assigned
print((lambda x,y: x+y)(2,4))