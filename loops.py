# while loop -- run as long as condition is true and we use while loop mostly when we don't know that how many time does this loop run
'''
count = 0
while  count <=4:
  print(count)
  count = count +1

count = 5
while  count >=0:
  print(count)
  count = count -1
else:
  print("while loop ended") '''

#for loop -- iterates over a sequence and we know that how many time does this iterate
# language = "python"
# for x in language:
#   print(x)

'''range function
range(stop(exclusive))
range(start,stop)
range(start,stop,step)'''

# for i in range(5):
#   print(i)

# for i in range(5,10):
#   print(i)

# for i in range(1,10,2):
#   print(i)

# for i in range(1,10,3):
#   print(i)

# for i in range(5):
#   print(i)
# else:
#   print("for loop ended") 


'''loop ctrl - pass statement'''
#1. pass statement
# for i in range(5):
  #mann nhi hai
  # pass

'''count =5
while count >0:
  if count == 3:
    pass # here jab count =3 hoga then then if condition true ho gyi so if condition k ander pass hai so it will    pass and it means for count =3 if wali statement true hai that's why else condintion nhi chalegi cuz if wali    condition wrong hogi then only else wali condition chalti h so it will pass to the (count -=1)
  else:
    print(count)
  count -=1 '''

'''loop ctrl - break statement'''
# for i in range(5):
#   if i ==3:
#     break # it terminated the iteration 
#   print(i)

'''loop ctrl - continue statement'''
# for i in range(5):
#   if i ==3:
#     continue # it skip the i ==3 iteration
#   print(i)


'''for i in range(5):
  if i ==3:
    break
  print(i)
print("---------")

for i in range(5):
  if i ==3:
    continue
  print(i) '''

'''infinite loop'''
# count = 5
# while count >0:
#   # print(count)
#   if count ==3:
#     continue
#   else:
#     print(count)
#   count -=1

# while True:
#   user_input = input("enter 'text to stop:")
#   if user_input == 'exit':
#     print("congrats! you guessed it right!")
#     break
#   print("sorry, you entered: ", user_input)


# Nested loop
