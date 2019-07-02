"""Hamming Distance between two numbers"""

def hamming_distance(x,y):

    # XOR operator to find the different bits  between two numbers
    different_bits = x ^ y
    count = 0
    while (different_bits > 0) :

        # masking the different bit with (0001) using bitwise & operator 
        masked_bits = different_bits & 1
        if (masked_bits != 0):
            count += 1
        #else shift all the bits to the right  by 1
        different_bits = different_bits >> 1
    return count