array = list(map(int,raw_input().split()))
result = 0
for i in array:
    result ^= array[i]
print result
