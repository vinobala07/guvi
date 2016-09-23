import collections
sentence = raw_input().split(' ')
mxm = 0
for word in sentence:
    count = collections.Counter(word)
    if max(count.values()) > mxm:
        mxm = max(count.items())
        max_word = word
print max_word
    
