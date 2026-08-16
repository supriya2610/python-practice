'''
def formate():
    f_name = input("Enter your first name: ")
    l_name = input("Enter your last name: ")
    result = f_name + " " + l_name
    return result.title()

# Correct call:
print(formate())
'''

def calculator():
 should_accumilate=True
 while True:
    a=float(input(f"enter the number?:"))
    operation=input("enter any  operation?\n +\n -\n *\n %\n:")
    b=float(input(f"enter the num2?:"))
    if operation == "+":
        return a+b
    if operation == "-":
        return a-b
    if operation == "*":
        return a*b
    if operation == "%":
        return a/b
    else:
        print("invalid operation entered")
print(calculator())
previous_value=calculator()
choice=input("enter if want to continue?Y or N:")
if choice=="Y":
   n1=previous_value
   should_accumilate=True

def add(n1,n2):
   return n1+n2
      
 