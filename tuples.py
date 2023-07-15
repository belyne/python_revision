my_tuple = (1, 'strings', 4.5, True)
tuple1 = 1, 'new', 3.4, False
print(my_tuple[1])
print(type(my_tuple))
print(type(tuple1))
print(my_tuple.count('strings'))
print(my_tuple.index(True))
for x in my_tuple:
    print(x)
