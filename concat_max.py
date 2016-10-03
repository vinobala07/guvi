def concatMax(A):
    A.sort(reverse = True)
    A = list(map(str,A))
    A = list(''.join(A))
    A.sort(reverse = True)
    c_pos = -3    
    while c_pos > 0-len(A):
        A.insert(c_pos,',')
        c_pos -= 4
    return ''.join(A)

if __name__ == '__main__':
    list_of_num = list(map(int,raw_input().split()))
    result = concatMax(list_of_num)
    print result    
