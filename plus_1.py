# Program to update an array of integers D to D+1, 
#ex:input <1,2,9>, output<1,3,0>

def plus_1(A):
    A[-1] += 1
    for i in reversed(range(len(A))):
        if A[i] != 10:
            break
        A[i]=0
        A[i-1] += 1
    if A[0] == 10:
        A[0] =1
        A.append(0)
    return A

