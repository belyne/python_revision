#def sum_of(a, b): takes only 2 number of arguments
   # return a + b
#print(sum_of(2, 4, 6)) but 3 were given 

def sum_of(*args):
    sum = 0
    for x in args:
        sum = sum + x
    return sum
print(sum_of(2, 4, 6, 7, 8))
