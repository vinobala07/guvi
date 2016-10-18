import math
def next_pow_2(n):
    if n-1 & n != 0:
        return 2**(int(math.sqrt(n))+1)
    return n

if __name__ == '__main__':
    n = input()
    print next_pow_2(n)


'''Write a function that, for a given no n, finds a number p which is greater than or equal to n and is a power of 2'''
