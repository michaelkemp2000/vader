# Defines a variable by adding a string with a data type which is assigned 10
x = "There are %d types of people." % 10

# Define a variable called binary and assign binary as value
binary = "binary"

# Define a variable called do_not and assign dont as value
do_not = "don't"

# Define a variable called v and assign a string that has two format chars assigned with
# associated values  (1).
y = "Those who know %s and those who %s." % (binary, do_not)

# Print content of x variable to screen
print x

# Print content of y variable to screen
print y

# Print string to screen that includes a formated char that displays data in x variable
# (2)
print "I said: %r." % x

# Print string to screen that includes a formated char that displays data in y variable
# (3)
print "I also said: '%s'." % y

# Create a variable and assign a boolean value of false.  Note: Capital F or T
hilarious = False

# Create variable and assign a formated character
joke_evaluation = "Isn't that joke so funny?! %r"

# Print the string via variable name and add the hilarious variable content through the
# formatted char (4)
print joke_evaluation % hilarious

# Define two variables with string content
w = "This is the left side of..."
e = "a string witha right side."

# Print both strings by adding them together like you would two numbers
print w + e