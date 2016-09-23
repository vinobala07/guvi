strng = list(raw_input())
i = 0
while(i < len(strng)-1):
    t = strng[i]
    strng[i] = strng [i+1]
    strng[i+1] = t
    i = i + 2
print ''.join(strng)
