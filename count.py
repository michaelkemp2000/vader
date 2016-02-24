import types

int_list = [1, 2, 3, 2, 2,]
float_list = [2.5, 1, 3, 2.5, 3.0]
string_list = 'this is nuts'

match_float = 2.5
match_string = ['nuts', 'is']
match_int = 2

def count(sequence, item):

    count = 0
    words = sequence.split()
    print words
    for s in words: 
        if (type(s) == types.IntType) and (type(item) == types.IntType): 
            if s == item:
                count += 1

        elif (type(s) == types.FloatType) and (type(item) == types.FloatType):
            if s == item:
                count += 1

        elif (type(s) == types.StringType) and (type(item) == types.StringType):
            if s == item:
                count += 1

        elif (type(s) == types.StringType) and (type(item) == types.ListType):
            for i in item:
                if s == i:
                    count += 1

        else:
            print "conditions not matched"
    
    print count

count(string_list, match_string)