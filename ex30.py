people = 30
cars = 40
busses = 15

if cars > people:
	print "We should take the cars."
elif cars < people:
	print "We should not take the cars."
else:
	print "We can't decide"

if busses > cars:
	print "Thats too many busses."
elif busses < cars:
	print "Maybe we should take the buses."
else: 
	print "We still can't decide."

if people > busses:
	print "Alright, lets just take the buses."
else:
	print "Fine, lets stay home then."