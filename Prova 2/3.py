def criarMatrizQuadrada(kTamanho = 3):
    matriz = []

    rangeTamanho = range(kTamanho)

    for i in rangeTamanho:
        matriz.append([])
        
        print('\nLinha ' + str(i + 1))
        
        for j in rangeTamanho:
            matriz[i].append(float(input('Elemento ' + str(j + 1) + ' da Linha ' + str(i + 1) + ': ')))

    return matriz

def somaMatriz(matriz1, matriz2):
    lenMatriz1, lenMatriz2 = len(matriz1), len(matriz2)
    
    if lenMatriz1 == 0:
        return matriz2
    if lenMatriz2 == 0:
        return matriz1
    if lenMatriz1 == 0 and lenMatriz2 == 0:
        return 0
    
    if lenMatriz1 == lenMatriz2:
        matriz = []
        
        for i in range(lenMatriz1):
            matriz.append([])
            for j in range(lenMatriz2):
                matriz[i].append(matriz1[i][j] + matriz2[i][j])
                
        return matriz
    
    return 0

def main():
    matriz3x3_1 = [[ 1,  2,  3], 
                   [ 4,  5,  6], 
                   [ 7,  8,  9]]
    
    matriz3x3_2 = [[ 2,  1,  2], 
                   [ 1,  2,  1], 
                   [ 2,  2,  2]]
    
    if input('Deseja criar as matrizes? ').lower() in ['y', 'yes', 's', 'sim']:
        print('Matriz 1')
        matriz3x3_1 = criarMatrizQuadrada()
        print('Matriz 2')
        matriz3x3_2 = criarMatrizQuadrada()
    
    print('Matriz 3x3 1:', matriz3x3_1)
    print('Matriz 3x3 2:', matriz3x3_2)
    print('Soma das Matrizes:', somaMatriz(matriz3x3_1, matriz3x3_2))  
        
main() 
