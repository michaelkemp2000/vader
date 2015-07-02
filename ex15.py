# Imports argv from Sys module (Class) - be able to take arguments in from command line
from sys import argv

# Put command line arguments into variables 
script, filename = argv

# Open a file and make txt a file object
txt = open(filename)

# Print text that lets you know that you the filename you are requesting
print "Here's your file %r." % filename

# Displays the content of the file
print txt.read()

# Asks if you want to see iy again
#print "Type the filename again:"
#file_again = raw_input(">")
#txt_again = open(file_again)
#print txt_again.read()

fileagain = raw_input("Enter the filename you want to open -->")
text_again = open(fileagain)
print text_again.read()

add_text = open(fileagain, 'w')
add_text.write("No, Fuck you asshole")



