# Function to reverse a string

def reverse(string):
    
    # init stores
    word = []
    rword = []
    char = ""
    answer = ""

    # abstract characters from string and store
    for s in string:
        word.append(s)
    
    # take from one store, reverse and place in another
    count = len(word)
    while count >= 1:
    	char = word[count -1]
    	rword.append(char)
    	count -= 1

    #Format back to readable
    for s in rword:
    	answer += s

    # return reversed string to function requester
    return answer

# Take a string as input
question = raw_input("Please provide a word: ")

# Get the string reversed and store
answer = reverse(question)

# print store
print answer