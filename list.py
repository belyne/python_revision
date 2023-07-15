list1 = [1, 2, 3, 4, 5]
list1[2] = 0
print(list1[2])
print(*list1)
print(list1, sep=" ")
list1.insert(len(list1), 6)
list1.append(7)
list1.extend([8, 9, 10, 11])
print(list1, end=" ")
print ()
del(list1[4])
list1.pop(8)
print(*list1)
list2 = ['a', 'b', 'c']
list3 = ['Hello', 1, True, 30.53]
list4 = [1, 2, 3, [list1], 14, 15]
print(*list4)
for i in list4:
    print(i)
