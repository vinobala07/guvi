import math
def two_set_bits(n):
    result = []
    end = int(math.sqrt(n))+1
    for i in range(end+1):
	for j in range(i+1,end+1):
            result.append(2**i+2**j)
    result.sort()
    return result

if __name__ == '__main__':
    n = input()
    result = two_set_bits(n)
    for i in result:
	print i,

