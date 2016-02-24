import re

# Takes text input and censors


def censor(text, word):

	# init stores
    words = []
    bword = []
    bw = ""
    answer = ""
    count = 0

    # Make String Lower
    low_text = text.lower()
    low_word = word.lower()
    
    # Convert string words in to list
    words = re.sub("[^\w]", " ", low_text).split()

    bword = re.sub("[^\w]", " ", low_word).split()

    # take from one store, reverse and place in another
    for w in words:
        if w in bword:
            bw = '*' * count
            words[count] = bw
        count +=1
                
#Format back to readable
    answer = ' '.join(words)
    return answer

# Take a string as input
question = raw_input("Please provide a word: ")

# Get the string without vowels and store
answer = censor(question, "sod")

# print store
print answer
