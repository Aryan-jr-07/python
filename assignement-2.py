# percentage calculator
'''
name = input("enter your name")
hindi =  input("enter hindi marks")
maths =  input("enter maths marks")
science = input("enter science marks")

percentage = ((int(hindi)+int(maths)+int(science))/300)*100
print(f"the result of {name} is {int(percentage)}%")
'''

# write a python program that collects multiple types of data eg name age height student name from user input ,stores them in a dictionary and then prints out the collected data?

user_data={}
# this is how u write key or element in dictonary
user_data["name"] = input("enter your name")
user_data["age"] = int(input("enter your age"))
user_data["height"] = float(input("enter your height"))
user_data["student"] = input("are you a student (yes/no)")
print(user_data)