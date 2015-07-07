tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print "printing escape char with debug.  It looks like: %r." % "this is a \t tab."
print "printing escape char with string.  It looks like: %s." % "this is a \t tab."
