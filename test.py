l1, l2 = [1, 10, 20], [50, 40, 30]
l3 = []

def combine_lists():
	x = 1
	for num in l1:
		l3.append(num)
	for num in l2:
		l3.insert(x, num)
		x +=2
	print l3

combine_lists()

def combine_list2():
	l1.extend(l2)
	l1.sort()
	print l1

combine_list2()

class Animal(object):
	pass

## Dog is-a Animal
class Dog(Animal):
	def __init__(self, name, bark):
		# Dog has-a name
		self.name = name
		self.bark = bark

	def say_hello(self):
		print self.bark

mydog = Dog("preston", "woof")
mydog.say_hello()