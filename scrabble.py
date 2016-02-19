# Dictionary of Scrabble leeters and associated score
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

# Function to total scrabble scores
def scrabble_score(word):

	#init stores
	total = 0
	f2_word = ""
	
	# Format word to lower case and alpha
	f1_word = word.lower()
	for let in f1_word:
		if let.isalpha():
			f2_word += let

    #Itterate through works and return total

	for char in f2_word:
		total += score[char]
	
	return total

# Take a string as input
word = raw_input("Please provide a word: ")

# Get the string without vowels and store
score = scrabble_score(word)

# print store
print score


    
