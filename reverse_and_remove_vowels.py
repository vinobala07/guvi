strng = raw_input()
vowels = ['a','e','i','o','u','A','E','I','O','U']
strng_list = list(strng)
strng_list.reverse()
strng = ''.join([l for l in strng_list if l not in vowels])
print strng
