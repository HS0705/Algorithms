#Find the number of times a letter appears in the word from 
#the given unique string of letters. 
#Ex: letter="aApP" word="Appears" output=4

def num_of_letters_in_word(letters,word):
    count = 0
    for letter in word:
        if letter in letters:
            count += 1
    return count
