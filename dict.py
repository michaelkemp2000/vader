my_dict = {
            "Name": "Michael",
            "Age": 39,
            "Height": 6.0
            }

print my_dict.items()
print my_dict.keys()
print my_dict.values()

for key in my_dict:
	print key, my_dict[key]

evens_to_50 = [i for i in range(51) if i % 2 == 0]
print evens_to_50

even_squares = [x**2 for x in range(1,11) if x % 2 == 0]

print even_squares

my_list = range(1, 11)
print my_list[::-1]


to_one_hundred = range(101)
# Add your code below!
backwards_by_ten = to_one_hundred[::-10]
print backwards_by_ten

print ""
print ""

to_21 = range(1, 22)
odds = to_21[::2]
middle_third = to_21[7:14:1]
print middle_third

print ""
print ""

languages = ["HTML", "JavaScript", "Python", "Ruby"]
test = lambda x: for x in x: if x == "Python": print x

print test(languages) 

