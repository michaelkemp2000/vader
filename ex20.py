from sys import argv

# Pass in an argument from command line
script, input_file = argv

# Function to print the whole file
def print_all(f):
	print f.read()

# Function to go the the begining of a file
def rewind(f):
	f.seek(0)

#Function to print a line of the file that you pass in
def print_a_line(line_count, f):
	print line_count, f.readline()

#Open file passed from the command line
current_file = open(input_file)

#Prints some text and print the whole file by passing calling the function that reads the whole file.
print "First let's print the whole file:\n"
print_all(current_file)

#Prints some text and calls the function that allows you to go the the begining of the file.
print "Now let's rewind, kind of like a tape."
rewind(current_file)

#Prints some text and then calls the functions that allow you to print one line of the file by passing the line of the file that you specify
#current line 1
print "Let's print three lines:"
current_line = 1
print_a_line(current_line, current_file)

#current line 2
current_line = current_line + 1
print_a_line(current_line, current_file)

#current line 3
current_line = current_line + 1
print_a_line(current_line, current_file)

