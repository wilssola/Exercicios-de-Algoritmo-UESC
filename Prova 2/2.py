def criarMatrizQuadrada(kTamanho = 5):
    matriz = []

    rangeTamanho = range(kTamanho)

    for i in rangeTamanho:
        matriz.append([])
        
        print('\nLinha ' + str(i + 1))
        
        for j in rangeTamanho:
            matriz[i].append(float(input('Elemento ' + str(j + 1) + ' da Linha ' + str(i + 1) + ': ')))

    return matriz

def listaMatrizDiagonal1Recursiva(matriz, index = 0):
    if len(matriz) <= 0:
        return []

    diagonal = matriz[0][index]    
    index += 1

    return [diagonal] + listaMatrizDiagonal1Recursiva(matriz[1:], index)

def listaMatrizDiagonal2Recursiva(matriz):
    if len(matriz) <= 0:
        return []

    diagonal = matriz[0][len(matriz) - 1]

    return [diagonal] + listaMatrizDiagonal2Recursiva(matriz[1:])

def obterMatrizDiagonais(matriz):
    diagonal1 = listaMatrizDiagonal1Recursiva(matriz)
    print(diagonal1)
    
    diagonal2 = listaMatrizDiagonal2Recursiva(matriz)
    print(diagonal2)
    
    return [diagonal1, diagonal2]

def main():
    matriz5x5 = [[ 1,  2,  3,  4,  5], 
                 [ 6,  7,  8,  9, 10], 
                 [11, 12, 13, 14, 15], 
                 [16, 17, 18, 19, 20], 
                 [21, 22, 23, 24, 25]]
    
    if input('Deseja criar a matriz? ').lower() in ['y', 'yes', 's', 'sim']:
       matriz5x5 = criarMatrizQuadrada()
       
    diagonais = obterMatrizDiagonais(matriz5x5)
    
    print('Matriz 5x5:', matriz5x5)
    print('Diagonais da Matriz 5x5:', diagonais)
    
main() 
