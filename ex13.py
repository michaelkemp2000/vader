from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first

print "Do you want to change this variable:", argv[1]
ans1 = raw_input()
print "Your second variable is:", second
print "Your third variable is:", third

