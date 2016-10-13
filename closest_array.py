import math
def closest_array(A,gvn):
    l = 0
    h = len(A)-1
    diff = float('-Inf')
    flag = False
    if gvn > A[h]:
        return h,True
    if gvn < A[l]:
        return l,True
    if gvn in A:
        return A.index(gvn),True
    while(l <= h):    
        if A[m]<gvn<A[m+1]:
            pos = m
            break
        if A[m-1] < gvn < A[m]:
            pos = m-1
            break
        if A[m+1] < gvn:
            l = m+1
            continue
        if A[m-1] > gvn:
            h = m-1
            continue
    return pos,flag 

if __name__ == '__main__':
    A = list(map(int,raw_input().split()))
    gvn = input()
    pos,flag = closest_array(A,gvn)
    if flag:
        print pos
    elif math.fabs(A[pos] - gvn) < math.fabs(A[pos+1] - gvn):
        print pos
    else:
        print pos+1
