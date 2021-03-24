normal = int(input('hora normal: '))
extra = int(input('hora extra: '))

sb = (10 * normal) + (15 * extra)
sl = sb * 0.9

print('salário bruto: R${:.2f}'.format(sb))
print('salário líquido: R${:.2f}'.format(sl))