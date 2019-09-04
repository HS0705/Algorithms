"""Hamming Distance between two numbers"""

def hamming_distance(x,y):

    # XOR operator to find the different bits  between two numbers
    different_bits = x ^ y
    print("different_bits"+ str(different_bits))
    count = 0
    while (different_bits > 0) :
        if (different_bits & 1):
            count += 1
        #else shift all the bits to the right  by 1
        different_bits = different_bits >> 1
        print("different_bits in loop"+str(different_bits))
        print("count"+str(count))
    return count

def spellBee(w1,w2):
    w1_list = list(w1)
    w2_list = list(w2)
    count = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            count += 1
    if count == 0:
            return True
    elif count > 0 and count <= 2:
         return "Almost There"
    else:
        return False

def oddNum():
    odd_num = []
    for i in range(0,10):
        if i%2 != 0:
            odd_num.append(i)
    return odd_num

def cowBull(s,g):
    cows = 0
    bulls =0
    s_list=list(s)
    g_list=list(g)
    for i in range(len(g_list)):
        if g_list[i] == s_list[i]:
            bulls += 1
        else:
            cows +=1
    return ("Hint is"+ str(cows) + "cows and" +  str(bulls) +"bulls")


def spellingBeeSolutions(wordlist, puzzles):
    # Write your code here
    output = []

    for puzzle in puzzles:
        for word in wordlist:
            count = 0
            for i in word:
                if i in puzzle and puzzle[0] in word:
                    count += 1
                break           
        output.append(count)
    return output
    