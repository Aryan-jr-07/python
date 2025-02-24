# calculator #

'''
# steps :-
1.function for operation
2.user input
3.print result
'''

''' setp 1'''
# fn to add two number
def add(num1,num2):
  return num1 + num2

#fn to sub two number
def sub(num1,num2):
  return num1 - num2

#fn to multiply two number
def multiply(num1,num2):
  return num1 - num2

#fn to divide two number
def divide(num1,num2):
  return num1 / num2

#fn to average two number
def avg(num1,num2):
  return (num1+num2)/2

''' setp 2 user input'''
print("please select a operation:\n" \
      "1. Addition\n" \
      "2. Substraction\n" \
      "3. Multiplication\n" \
      "4. Division\n" \
      "5. Average\n")

select = int(input("select a opeation from 1,2,3,4,5: "))

number1 = int(input("Enter first number"))
number2 = int(input("Enter second number"))

'''step 3 print result'''
if select == 1:
  # print("Sum of two number is :", add(number1, number2))
  print(number1, "+", number2, "=", \
        add(number1, number2))
elif select == 2:
    print(number1, "-", number2, "=", \
          sub(number1, number2))
elif select == 3:
    print(number1, "*", number2, "=", \
          multiply(number1, number2))
elif select == 4:
    print(number1, "/", number2, "=", \
          divide(number1, number2))
elif select == 5:
    print("(", number1, "+", number2, ")", "/", "2", "=", \
          avg(number1, number2))
else:
   print("Invalid operation! pls select again")

   