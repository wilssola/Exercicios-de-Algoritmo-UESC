length = int(input('quantidade: '))
numbers = [None] * length

for i in range(len(numbers)):
    numbers[i] = float(input('número{:}: '.format(i + 1)))

numbers = sorted(numbers)

total = 0
for i in numbers:
    total = total + i

print('menor: ' + str(numbers[0]))
print('maior: ' + str(numbers[len(numbers) - 1]))
print('media: ' + str(total / len(numbers)))