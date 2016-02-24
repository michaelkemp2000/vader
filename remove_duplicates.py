from collections import OrderedDict
import types

int_list = [1, 2, 3, 2, 2]
float_list = [2.5, 1, 3, 2.5, 3.0]
string_list = 'this is nuts'

match_float = 2.5
match_string = ['nuts', 'is']
match_int = 2

def remove_duplicates(sequence):

	return dict.fromkeys(sequence).keys()

seq = remove_duplicates(int_list)
print seq

