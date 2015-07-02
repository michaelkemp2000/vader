import pdb

prompt = "---->"

print "How old are you?",
age = raw_input(prompt)

print "How tall are you?",
height = raw_input(prompt)
pdb.set_trace()
print "How much do you weigh?",
weight = raw_input(prompt)

print "So, you're %r old, %r tall an %r heavy." % (age, height, weight)