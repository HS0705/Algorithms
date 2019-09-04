"""  Reverse a string inplace without using built in reverse"""

def reverse(a_list):
    left_index = 0
    right_index = len(a_list) - 1
    while left_index < right_index:
        a_list[left_index],a_list[right_index] = a_list[right_index], a_list[left_index]
        left_index += 1
        right_index -= 1
    return a_list


def uniqueMorseRepresentations(words):
        hash_map = set()
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for word in words:
            word_morse = ""
            for char in word:
                word_morse += morse[ord(char)-97]
            hash_map.add(word_morse)
        return len(hash_map)

def numUniqueEmails(emails):
        unique_emails = set()
        for email in emails:
            local_name, domain_name = email.split('@')
            if '+' in local_name:
                local_name = local_name.split('+',1)[0]
            local_name = local_name.replace('.','')
            unique_emails.add(local_name + '@'+ domain_name)
            print(unique_emails)
        return len(unique_emails)
    
def peakIndexInMountainArray(A):
        if len(A) >=3:
            for i in range(0,len(A)-1):
                if A[i] > A[i+1]:
                    print(i)
                    return i 
        else:
            return 0

def outer_parentheses(S):
    counter = 0
    start_index = 0
    l = []
    for i in range(len(S)):
        if S[i] == '(':
            counter += 1
        else:
            counter -= 1
        if counter == 0:
            l.append(S[start_index+1:i])
            start_index = i+1
    return ''.join(l)