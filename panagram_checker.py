import re
def pangram_checker(strng):
    word = ''.join(re.findall('[a-zA-Z]+',strng))
    word = word.lower()
    if len(set(list(word))) == 26:
        print 'pangram'
    else:
        print 'not a pangram'

if __name__ == '__main__':
    sentence = raw_input()
    pangram_checker(sentence)
