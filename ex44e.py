#Composition vs. Inheritance.

class Other(object):

	def overide(self):
		print "OTHER overide()"

	def implicit(self):
		print "IMPLICIT overide()"

	def altered(self):
		print "ALTERED overide()"

class Child(object):

	def __init__(self):
		self.other = Other()

	def implicit(self):
		self.other.implicit()

	def overide(self):
		print "CHILD overide()"

	def altered(self):
		print "CHILD before OTHER, altered()"
		self.other.altered()
		print "CHILD after OTHER, altered()"

son = Child()

son.implicit()
son.overide()
son.altered()


