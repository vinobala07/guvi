array = list(map(int,raw_input().split()))
rotate = input()
for i in range(rotate):
    array.insert(0,array.pop())
print array

