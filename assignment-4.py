#1. limit the decimal places to 2 digit using formate method and print result, for the variable pi = 3.14159265359

''' pi = 3.14159265359
print(round(pi,2))
print("value of pi is {}".format(pi))
print("value of pi is {:.2f}".format(pi))  # (.2f) this will do round of the decimal to only two
print("value of pi is {:.1f}".format(pi))  # (.1f) this will do round of the decimal to only one
print("{:.4f}".format(pi))  # (.4f) this will do round of the decimal to only four '''

#2. Extract characters from index 2 to 8 with a step of 2: given my_string = "python course", slice character from index 2 to 8, skipping every other character.
''' my_string = "python course"
print(my_string[2:8:2]) '''
 
#3.slice to get only the middle character(S):for my_string= "madhav", use slicing to extract the middle character(s).
'''my_string = "madhav"  # 6 chars - even
my_string2= "madhava" # 7 char -odd
def mid_str(word):
  middle = int(len(word)/2)
  if len(word)%2 ==0:
    return word[middle-1 : middle+1]
  else:
    return word[middle]
print(mid_str(my_string))'''

#4.remove the first 3 and last 3 characters: given my_string= "Regression analysis", remove the first 3 abd last 3 characters.
'''my_string= "Regression Analysis"
# string[start:stop:step]
print(my_string[3:-3])'''

#5. get the substring that starts 4 characters from the end to the last character: for my_string = "classification", slice the string starting from the 4th character from the end to the last character.
'''my_string ="classification"
print(my_string[-4:])'''

#6. How to reverse a string using python string methods?
'''word = "Python"
print(word[::-1])'''

#7. Write a python function to check if a string is a palindrome using string method
'''word = "madam"
word2 = "madan"
def is_palindrome(s):
  if s == s[::-1]:
    print(f"{s} is a palidrome")
  else:
    print(f"{s} is not a palindrome")
is_palindrome(word)
is_palindrome(word2)'''

