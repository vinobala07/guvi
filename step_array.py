step_array = list(map(int,raw_input().split(' ')))
i = 0
while i < (len(step_array)-1) and step_array[i]!= 0:
    i += step_array[i]
if i == len(step_array)-1:
    print True
else:
    print False
