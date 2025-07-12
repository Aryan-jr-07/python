# 1. if statement 
'''
a = 26
b= 108
if b>a:
    print("b is greater that a")

#2. if -else statement
age = int(input("enter your age:"))
if age >29:
    print("you are adult")
else:
    print("you are not adult")

temp = int(input("enter temperature:"))
if temp <30:
    print("it's a cold day")
else:
    print("it's a hot day")

    
#2. if -elif-else statement
marks = int(input('enter your marks :'))
if marks >= 80:
    print("grade A")
elif marks >=70:
    print("grade B")
elif marks >=50:
    print("grade C")
else:
    print("grade d")

# 4. nested if else 
#Q; positive, negative & zero. positive - even/odd
number = int(input("enter a number :"))
if number >0:
    if number%2 == 0:
        print("this is an even number")
    else:
        print("this is an odd number")
else:
    if number == 0:
        print("this is a zero")
    else:
        print("this is a negative number")


# 5. conditional expression (ternary operator)
age = int(input("enter you age :"))
status = "major" if age >= 18 else "minor"
print(status)
'''

