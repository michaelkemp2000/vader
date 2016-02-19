# Takes text input and returns woth no vowels

def anti_vowel(string):

	# init stores
    word = []
    rword = []
    char = ""
    answer = ""
    count = 0

    # Make String Lower
    low_string = string.lower()
    
    # abstract characters from string and store
    for s in low_string:
        word.append(s)

    # take from one store, reverse and place in another
    while count < len(word):
        char = word[count]
        print char
        if char not in ('a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'):
    	   rword.append(char)
    	count += 1

    #Format back to readable
    answer = ''.join(rword)
    return answer

# Take a string as input
question = raw_input("Please provide a word: ")

# Get the string without vowels and store
answer = anti_vowel(question)

# print store
print answer

