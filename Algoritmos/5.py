import math

x = [float(input('xA: ')), float(input('xB: '))]
y = [float(input('yA: ')), float(input('yB: '))]

distance = math.sqrt(((x[1] - x[0]) ** 2) + ((y[1] - y[0]) ** 2))
print('distância: ' + str(distance))