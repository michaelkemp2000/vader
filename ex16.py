from sys import argv

script, filename = argv

print "We're going to erase %r." % filename

print "If you don't wan tto do that, hit CTRL-C."

print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file.  Goodbye!"
target.truncate()

print "Now I'm asking you for three lines."

line1 = raw_input("Line 1:")
line2 = raw_input("Line 2:")
line3 = raw_input("Line 3:")

print "I'm going to write these to the file..."

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

print "And finally, we close it."
target.close()

# Read the file we just created
print "reading new file content"
target = open(filename)
data = target.read()
print "here it is:"
print data
print "closing file..."
target.close()

