start = input()
end = input()
flag = count = 0
if start > end:
    start,end = end , start
if start == 1:
    start += 1
if start == 2:
    count += 1
    start += 1
for i in range(start,end+1):
    flag = 0
    for j in range(2,i/2+1):
        if(i%j == 0):
            flag = 1
            break
    if flag != 1:
        print i
        count += 1
print count
