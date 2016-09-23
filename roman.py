roman_numbers = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
roman = raw_input().upper()
length = len(roman)
i = length-1
sum = 0
while(i > 0):
    if roman_numbers[roman[i]] > roman_numbers[roman[i-1]]:
        sum = sum + roman_numbers[roman[i]]-roman_numbers[roman[i-1]]
        print sum
        i = i-2
    elif roman_numbers[roman[i]] < roman_numbers[roman[i-1]]:
        sum = sum + roman_numbers[roman[i-1]]+roman_numbers[roman[i]]
        print sum
        i = i-2
    else:
        sum = sum + roman_numbers[roman[i]]
        print sum
        i = i-1
if i == 0:
    sum = sum + roman_numbers[roman[0]]
print sum
        
