my_d = {}
print(type(my_d))

my_dict = {1: 'Test', 'Name': 'Jim', 1: 'Not a Test'}
print(my_dict)
my_dict[2] = 'Test 2'
my_dict[1] = 'Not a Test'
print(my_dict)
for y in my_dict:
    print(y)

for key, value in my_dict.items():
    print(str(key) + " : " + value)
