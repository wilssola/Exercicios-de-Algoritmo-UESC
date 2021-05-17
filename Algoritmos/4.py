inputs = [None] * 20
equals = 0
larger = 0
smaller = 0

for i in range(len(inputs)):
    inputs[i] = int(input('n' + str(i + 1) + ': '))
    if inputs[i] == inputs[0] and i != 0:
        equals = equals + 1
    if inputs[i] > inputs[0]:
        larger = larger + 1
    if inputs[i] < inputs[0]:
        smaller = smaller + 1

print('iguais: ' + str(equals))
print('maiores: ' + str(larger))
print('menores: ' + str(smaller))