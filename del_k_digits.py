def del_k_digits(numbr,k):
    A = list(str(numbr))
    A.sort()
    return ''.join(A[:-k])

if __name__ == '__main__':
    numbr = input()
    k = input()
    if k > len(list(str(numbr))):
        print 'not possible'
    else:
        print del_k_digits(numbr,k)
