number = int(input('número: '))

for i in range(10):
    local = i + 1
    print('{:} * {:} = {:}'.format(number, local, number * local))