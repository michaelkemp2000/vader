## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

## Dog is-a Animal
class Dog(Animal):
	def __init__(self, name, bark):
		# Dog has-a name
		self.name = name
		self.bark = bark

	def say_hello():
		print self.bark

## Cat is-a Animal
class Cat(Animal):

	def __init__(self, name):
		# Cat has-a name
		self.name = name

# Person is-a Object
class Person(object):

	def __init__(self, name):
		# Person has-a name
		self.name = name

		# Person has a pet of some kind
		self.pet = None

# Employee is-a person
class Employee(Person):

	def __init__(self, name, salary):
		## hmm whats this strange magic?  Inherit name from person maybe?
		super(Employee, self).__init__(name)
		#  Emplyee has-a Salary
		self.salary = salary

# Fish is-a Object
class Fish(object):
	pass

# Salmon is-a Fish
class Salmon(Fish):
	pass

# Halibut is-a Fish
class Halibut(Fish):
	pass

## rover is-a Dog
#rover = Dog("Rover")

# satan is-a Cat
satan = Cat("Satan")

# Mary is-a Person
mary = Person("Mary")

# Mary has-a Pet instance called Satan
mary.pet = satan

#Frank is-a Employee that has-a salary of 120000
frank = Employee("Frank", 120000)

#Frank has a pet called rover
#frank.pet = rover

#Flipper is-a Fish
flipper = Fish()

#Crouse is-a Salmon
crouse = Salmon()

#Harry is a Halibut
harry = Halibut()

mydog = Dog("preston", "woof")
mydog.say_hello()

