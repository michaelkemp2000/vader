#Create a mapping of states
states = {
	'Oregan': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}

#create a basic set of states an some cities in them
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

#add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
print '-' * 10
print "NY state has: ", cities['NY']
print "OR State has: ", cities['OR']

#print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

#print every abbreviation
print '-' * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)

#print every city nstate
print '-' * 10
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)

#now do both at the same time
print '-' * 10
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print '-' * 10
#saftly get an abbreviation by state that might not be there
state = states.get('Texas', None)

if not state:
	print "Sorry, no Texas."

#get a city with default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city	

#Compare dictionaries

print "Return Value : %d" %  cmp(cities, states)
ret_value = cmp(cities, states)
if ret_value == -1:
	print "no match"

#print length of dicstionary

print "Length : %d" % len (cities)

#Print dict out as string

print "Equivalent String : %s" % str (cities)

#Show the variable types in a dict

print "Variable Type : %s" %  type (cities)

#copy a dict and print

cities2 = cities.copy()
print "New Dictionary : %s" %  str(cities2)

#clear a dict

print "Start Len : %d" %  len(cities2)
cities2.clear()
print "End Len : %d" %  len(cities2)

