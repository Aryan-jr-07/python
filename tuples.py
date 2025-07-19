'''Tuples'''
# tuple are immutable means it is not changeble

'''mutliple way to creare tuples'''

# 1. using pranthesis -- just write inside small bracket
# hehe = (1,2,[99,27],(3,4),"siuu")

# 2. without pranthesis -- just write anything it should be comma seperated
# hehe = 1,2,3,"siuu",99

# 3. using tuple constructor
# new_tup = tuple((1,2,"hello","siuuu","maggie"))
# if u want to convert list in tuple 
# new_dawg = [1,2,3,4,"man"]
# new_shit = tuple(new_dawg)

# 4. single item tuple
# new_top = ("singleeonly",)
# new = 4,

# huh = (1,2,3,4,"aag")
# print(huh)
# print(type(huh))

'''contatinations'''
# tup = ("sike",22,"khaa")
# sup = ("laida",99,"farebi")
# print(tup+sup)

'''repetations'''
# huhu = ("hel",) * 3
# print(huhu)

'''chekc for an item'''
# num = (1,2,3,99,77,29,79)
# print(num)
# print(type(num))
# print(99 in num)


# siuu =("hmm","lamine","yamal","siuu")
# i= 0
# while i < len(siuu):
#     print(siuu[i])
#     i +=1


'''tuple method'''
# there are only two method in tuple --- count() and index()
# count() in tuple means u can get the number of times that value occurs in a tuple
# index() it will return you the index number of that value whichever you search in the .index()

kajal = ("teri","ek","gul","dil","gul","gul")
print(kajal.count("gul"))
