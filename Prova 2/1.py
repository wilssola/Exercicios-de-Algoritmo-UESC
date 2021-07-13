def intercalarListas(lista1, lista2, lista3):
    lenLista1, lenLista2, lenLista3 = len(lista1), len(lista2), len(lista3)
    
    if lenLista1 == 0 and lenLista2 == 0 and lenLista3 == 0:
        return []
    
    return ([lista1[0]] if lenLista1 > 0 else []) + ([lista2[0]] if lenLista2 > 0 else []) + ([lista3[0]] if lenLista3 > 0 else []) + intercalarListas((lista1[1:] if lenLista1 > 0 else []), (lista2[1:] if lenLista2 > 0 else []), (lista3[1:] if lenLista3 > 0 else []))

def main():
    lista1 = [1, 4, 7]
    lista2 = [2, 5, 8]
    lista3 = [3, 6, 9]
    print(intercalarListas(lista1, lista2, lista3))
    
    lista1 = ['1', '4', '7']
    lista2 = ['2', '5', '8']
    lista3 = ['3', '6', '9']
    print(intercalarListas(lista1, lista2, lista3))
    
    lista1 = ['Pão', 'Batata', 'Frango']
    lista2 = ['Sal']
    lista3 = ['Arroz', 'Trigo', 'Feijão']
    print(intercalarListas(lista1, lista2, lista3))
    
    lista1 = [1, 2]
    lista2 = ['Sal', 3]
    lista3 = []
    print(intercalarListas(lista1, lista2, lista3))
        
main()
