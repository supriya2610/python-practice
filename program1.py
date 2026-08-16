'''
with open("todolist.txt","r") as f:
 print(f.read())
'''
'''
f=open("todolist.txt","r")
print(f.readline())
print(f.readline())
print(f.readline())## this will print single line at once we can call it multiple time then it will call next line 
f.close()
'''

with open("todolist.txt", "a") as f:
  f.write("Now the file has more content!")
with open("todolist.txt") as f:
  print(f.read())