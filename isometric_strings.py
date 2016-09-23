import collections
a = raw_input()
b = raw_input()
c = collections.Counter(a)
d = collections.Counter(b)
flag = 1
if len(a)!= len(b):
    print False
else:
    for i in range(len(a)):
        if c[a[i]] != d[b[i]]:
            flag = 0
            break
    if flag == 0:
        print False
    else:
        print True
