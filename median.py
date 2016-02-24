int_list = [1, 2, 3, 2, 2]

def median(sequence):
    
    sequence.sort()

    if len(sequence) % 2 == 1:
        return sequence[len(sequence)/2]
    else:
        return (sequence[len(sequence)/2]+sequence[len(sequence)/2 -1])/2.0

seq = median(int_list)
print seq