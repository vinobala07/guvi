def returnIndex(A):
    for i, ele in enumerate(A):
        if i == ele:
            return ele
    return -1

if __name__ == '__main__':
    array = list(map(int,raw_input().split()))
    print returnIndex(array)
        
