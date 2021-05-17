money = 1200
c1 = 200
c2 = 120

result = money - ((c1 + (c1 * 0.02)) + (c2 + (c2 * 0.02)))
print('R${:.2f}'.format(result))