import re
def panagram_checker(strng):
    word = ''.join(re.findall('[a-zA-Z]+',strng))
    word = word.lower()
    if len(set(list(word))) == 26:
        print 'panagram'
    else:
        print 'not a panagram'

if __name__ == '__main__':
    sentence = raw_input()
    panagram_checker(sentence)
