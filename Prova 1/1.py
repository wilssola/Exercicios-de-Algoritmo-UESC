def cria_sublista(lista, M, N):
    sublista = lista[(M-1):(N)]
    return sublista

def main():
    quantidade = int(input("Quantos números pretende adicionar? "))

    lista = []

    for i in range(quantidade):
        lista.append(int(input("Número " + str(i + 1) + ": ")))

    M = int(input("\nQual o primeiro Número pretende tirar? "))
    N = int(input("Qual o último Número pretende tirar? "))

    print("\nSublista:")
    print(cria_sublista(lista, M, N))

main()
