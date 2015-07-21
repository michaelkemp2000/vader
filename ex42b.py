#Override Explicitly
#Child class with same function is used not the parent one.

class Parent(object):

	def overide(self):
		print "PARENT overide()"

class Child(Parent):

	def overide(self):
		print "CHILD override()"

dad = Parent()
son = Child()
dad.overide()
son.overide()
