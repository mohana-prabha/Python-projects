def sum(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def divide(x,y):
    if y==0:
        return "Division by zero not possible" 
    return x/y 
print("welcome to calculator program (for 2 numbers only)")
while True:
    print("Enter 1 to add")
    print("Enter 2 to subtract")
    print("Enter 3 to multiply")
    print("Enter 4 to divide")
    print("Enter 5 to exit from the calculator")
    choice=int(input("Enter your choice ="))
    num1=int(input("Enter first number ="))
    num2=int(input("Enter second number ="))
    if (choice==1):
        print("Result : ",sum(num1,num2))
    elif(choice==2):
        print("Result : ",sub(num1,num2))
    elif(choice==3):
        print("Result : ",mul(num1,num2))
    elif(choice==4):
        print("Result : ",divide(num1,num2))
    elif(choice==5):
        break
    else:
        print("Enter the valid input")       