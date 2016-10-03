import math
def repeatedNumber(A):
    A = list(A)
    rep_list = []
    for i in range(len(A)):
        if A[int(math.fabs(A[i]))] >= 0:
            A[int(math.fabs(A[i]))] = 0 - A[int(math.fabs(A[i]))]
        else:
            rep_list.append(int(math.fabs(A[i])))
    return rep_list

if __name__ == '__main__':
    print repeatedNumber([1,2,3,4,5,1,2,3])
