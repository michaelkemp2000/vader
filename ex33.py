
numbers = []
i = 0
prompt = '-->'

def while_loop(number, number1):
	#Leveraging a variable that is defined outside of this function
	global i

	while i < number:
		print "At the top i is %d" % i
		numbers.append(i)

		i += number1
		print "Numbers now:", numbers
		print "At the bottom i is %d" % i

def start():
	print "Pass in a number"
	no = raw_input(prompt)
	print "Pass in an incrementer"
	nu = raw_input(prompt)
	while_loop(int(no), int(nu))
	for_loop()

def for_loop():
	print "The numbers:"

	for num in numbers:
		print num
start()
