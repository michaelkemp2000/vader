#Special case overide

class Parent(object):

	def altered(self):
		print "PARENT Altered()"

class Child(Parent):

	def altered(self):
		print "CHILD before PARENT altered()"
		super(Child, self).altered()
		print "CHILD after PARENT altered()"

dad = Parent()
son = Child()
dad.altered()
son.altered()