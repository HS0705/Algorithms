"""  Reverse a string inplace without using built in reverse"""

def reverse(a_list):
    left_index = 0
    right_index = len(a_list) - 1
    while left_index < right_index:
        a_list[left_index],a_list[right_index] = a_list[right_index], a_list[left_index]
        left_index += 1
        right_index -= 1
    return a_list