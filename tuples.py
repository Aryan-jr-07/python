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
''' kajal = ("teri","ek","gul","dil","gul","gul")
print(kajal.count("gul"))''' # output: 3

# index() it will return you the index number of that value whichever you search in the .index()
''' players = "dalle","nalla","mamta","sanjay","pu",1
print(players.index(1)) # output: 5
print(type(players)) '''

# tuple functions :- (len, sorted, sum, max, min)
''' huhu = ("hass","dii","ronaldo",13,4,4,88,23,79)
print(len(huhu)) '''

'''mar = (1,2,45,6,69,7,47,99)
# print(sum(mar)) # output: 276 (which is sum of all the numbers in the give tuple)
# print(max(mar)) # output: 99 (max number in the tuple)
# print(min(mar)) # output: 1 (lowest number in the tuple)

siuu = sorted(mar) #sorted in python changes the tuple into list
print(siuu)
print(type(siuu))

sike = tuple(siuu) # if u want to change the list into tuple again
print(sike)
print(type(sike))'''



# packing and unpacking in tuple :---
''' packing -- Packing is putting multiple values into a single tuple variable.'''
# a = "Aryan"
# b= 19 
# c ="stricker"
# t_pack = a,b,c
# print(t_pack)
# print(type(t_pack))

''' unpacking -- we unpack '''
# name , age , proff = t_pack
# print(name)
# print(age)
# print(proff)
# print(type(name))
# print(type(age))
# print(type(proff))


'''packing'''
# packed = 1, 2, 3, 'hello'
# print(packed)
# print(type(packed))

'''unpacking'''
# a, b, c, d = packed
# print(a)  # 1
# print(b)  # 2
# print(c)  # 3
# print(d)  # 'hello'




# Modifying tuples
''' tuple_number = (10,40,99)
tuple_number[0] =100 #it will thorugh an (error) as tuple is immutable(not_changeable)'''

''' How to mutate / modify tuple ''' 
#  So the answer is first change the tuple into list then do modification then chnage back it to tuple'''

# new = list(tuple_number)
# print(new)
# new[0]=130
# new.extend(["hehe",99])
# print(new)
# print(type(new))

# tuple_number = tuple(new)
# print(tuple_number)
# print(type(tuple_number))