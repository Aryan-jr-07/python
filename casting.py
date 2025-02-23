a = "1"
print(type(a))
b = 12
print(type(b))

# if u want to change the type of the given variable then u can use the following methods

c = int(b) 
print(type(c))

print(int(a)+b)

''''
name = "madhav"
newname = int(name)  # all str type can't be casted into numerical type
print(newname) '''

f1 = 22.56
print(type(f1))
print(type(int(f1)))


# implicit type casting
var1 = 10 # int type
var2 = 20.5 #float type
print(var1+var2)
print(int(var1+var2))

# explicit type casting
ok = 101
s =  str(ok)
print(type(s))

a0 = bool(0)
print(type(a0))
print(a0)

a1 = bool(1)
print(type(a1))
print(a1)