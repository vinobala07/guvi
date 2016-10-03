def unique_ele(A):
    result = 0
    for i in A:
        result ^= i
    return result
if __name__ == '__main__':
    array = list(map(int,raw_input().split()))
    print unique_ele(array)
