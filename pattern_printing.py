# Left-Aligned Right-Angled Triangle
'''n =10
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()'''

# shortcut
'''n =6
for i in range(1,n+1):
    print(" * "*i)'''




# inverted Triangle
'''n = 50
for i in range(n,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()'''

# shortcut
'''n= 10
for i in range(n,0,-1):
    print(" * "*i)'''




# pyramid pattern
n=5
for i in range(1,n+1):
    print(" " * (n-i),end=" ") #for gap
    print("*" * (2*i-1))










# # Left-Aligned Right-Angled Triangle
# n = 5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
# print("-----")
# # # shortcut
# n =6 
# for i in range(1,n+1):
#     print("* "*i)



# inverted Triangle
# n = 5
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

# # shortcut
# n=5
# for i in range(n,0,-1):
#     print("* "*i)



# # inverted Triangle
# n = 6
# for i in range(1,n+1):
#     print(" " *(n-i),end=" ")
#     print("*"* (2*i-1))
