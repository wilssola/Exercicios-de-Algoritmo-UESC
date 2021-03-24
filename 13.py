length = int(input('quantidade: '))
numbers = [None] * length

for i in range(len(numbers)):
    numbers[i] = float(input('salário{:}: '.format(i + 1)))    
    if numbers[i] < 5000:
        numbers[i] = numbers[i] + (numbers[i] * 0.3)
        print('salário{:} aumento: {:}'.format(i + 1, numbers[i]))