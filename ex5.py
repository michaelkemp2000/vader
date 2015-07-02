name = 'Michael Kemp'
age = 38 
height = 74 # inches
weight = 215 # lbs
eyes = 'Blue'
teeth = 'Yellow'
hair = 'Brown'

print "Let's talk about %r." % name
print "He's %d inches tall." % height
print "He's %d prounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

print "if I add %d, %d, and %d I get %d." % (
	age, height, weight, age + height + weight)
	
inches = 72
centimeters = inches / 0.39370
pounds = 215
kilos = pounds / 0.453592

print "%f inches = %f centimeters." % (inches, centimeters)
print "%f pounds = %f kilos." % (pounds, kilos)


	