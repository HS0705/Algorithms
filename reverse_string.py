"""Reverse a given string"""

def reverse_string(string1):

    #splits the string into a list
    words_list = string1.split(' ')
    reversed_list = []
    for word in words_list:
        reversed_list.append(word[::-1])
    return ' '.join(reversed_list)