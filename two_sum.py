"""Two Sum Problem - return the indoces of the two numbers that add upto the target sum"""

def two_sum(num_list, target_sum):
    dict = {}
    for i in range(len(num_list)):
        num1 = num_list[i]
        num2 = target_sum - num1
        if num1 in dict:
            return [dict[num_list[i]],i]
        else:
            dict[num2]=i