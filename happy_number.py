number = input()
sum = 0
while (number > 9):
    while number > 0:
        sum = sum + pow(number%10,2)
        number /= 10
    number = sum
    sum = 0
if number == 1:
    print 'happy'
else:
    print 'not happy'
