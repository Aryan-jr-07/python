
# 1.Question
# value = None
# if value:
#     print("value is true")
# else:
#     print("value is false")

#2. Question
# write a simple program to determine if a given year is a leap year using user input

''' 
condition:-
4 divisible & 100 not divisible
400 divisible
'''
# year = int(input("enter a year:"))
# if year % 4 == 0 and year % 100 !=0 or (year % 400 == 0):
#     print(f"{year} is a leap year")
# else:
#     print(f"this {year} is not leap year")

# 3. Question
'''
login authentication using cinditional statement. assume u have a predefined username and password ''' 

# predefined_username = "Aryan"
# predefined_password = "siu07"

# username =input("enter your username :")
# password = input("enter your password :")
# if username == predefined_username:
#     if password == predefined_password:
#         print("welcome to the page")
#     else:
#         print("invalid password")
# else:
#     print("invalid username")

# 4. Question
Maths_marks = int(input("enter your maths marks :"))
Physics_marks = int(input("enter your physics marks :"))
Chemistry_marks = int(input("enter your chemisry marks :"))
if (Maths_marks >= 65 and Physics_marks >=55 and Chemistry_marks >= 50 and (Maths_marks+Physics_marks+Chemistry_marks) >= 180)or (Maths_marks+Physics_marks) >=140:
    print("Eligible for admission")
else:
    print("your are not Eligible ")