class Parent(object):

	def implicit(self):
		print "Parent implicit()"

	def overide(self):
		print "PARENT overide()"

	def altered(self):
		print "PARENT Altered()"

class Child(Parent):

	def overide(self):
		print "CHILD override()"

	def altered(self):
		print "CHILD before PARENT altered()"
		super(Child, self).altered()
		print "CHILD after PARENT altered()"

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
dad.overide()
son.overide()
dad.altered()
son.altered()