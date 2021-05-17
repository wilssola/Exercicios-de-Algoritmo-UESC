inputs = [None] * 5

for i in range(5):
    inputs[i] = int(input('n' + str(i + 1) + ': '))

inputs = sorted(inputs)
smaller = inputs[0]
larger = inputs[len(inputs) - 1]

print('menor: ' + str(smaller))
print('maior: ' + str(larger))