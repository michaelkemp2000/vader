#Looks OK

def break_words(stuff):
    "This function will break up words for us."
    words = stuff.split(' ')
    return words

#Looks OK
def sort_words(words):
    "Sorts the words."
    return sorted(words)

#Fixed : on first line... fixed poop to pop ...
def print_first_word(words):
    "Prints the first word after popping it off."
    word = words.pop(0)
    print word

#Fixed ) on line 22.
def print_last_word(words):
    "Prints the last word after popping it off."
    word = words.pop(-1)
    print word

#Looks OK
def sort_sentence(sentence):
    "Takes in a full sentence and returns the sorted words."
    words = break_words(sentence)
    return sort_words(words)

#Looks OK
def print_first_and_last(sentence):
    "Prints the first and last words of the sentence."
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

#Looks Ok
def print_first_and_last_sorted(sentence):
    "Sorts the words then prints the first and last one."
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""


print "--------------"
print poem
print "--------------"

# Bad sum, fixed
five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

#division symbol was wrong on line 70.
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
#Fixed == to =. changes staring-point to starting_point
beans, jars, crates = secret_formula(start_point)

#Typo --- bjeans, not beans
print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

# Fixed Typo and start_point
print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)

#Typos
sentence = "All good things come to those who wait."

words = break_words(sentence)
sorted_words = sort_words(words)

print_first_word(words)
print_last_word(words)
print_first_word(sorted_words)
print_last_word(sorted_words)
sorted_words = sort_sentence(sentence)
print sorted_words

print_first_and_last(sentence)

print_first_and_last_sorted(sentence)
