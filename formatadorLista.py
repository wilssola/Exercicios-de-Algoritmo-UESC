def formatadorLista(quantidade):
    lista = []

    for i in range(quantidade):
        numero = float(input("Número " + str(i + 1) + ": "))
        lista.append(numero)  

    # A
    def maior(lista):
        lista.sort()
        return lista[-1]
    print("Maior Elemento:", maior(lista))

    # B
    def soma(lista):
        soma = 0
        for i in lista:
            soma += i
        return soma
    print("Soma Elementos:", soma(lista))

    # C
    def iguaisPrimeiro(lista):
        iguaisPrimeiro = -1
        for i in lista:
            if i == lista[0]:
                iguaisPrimeiro += 1
        return iguaisPrimeiro
    print("Total Elementos = lista[0]:", iguaisPrimeiro(lista))

    # D
    def media(soma, quantidade):
        return soma / quantidade
    print("Média Elementos:", media(soma(lista), quantidade))

    # E
    def mediaAproximada(soma, quantidade):
        return soma // quantidade
    print("Média Aproximada Elementos:", mediaAproximada(soma(lista), quantidade))

    # F
    def somaNegativa(lista):
        somaNegativa = 0
        for i in lista:
            if numero < 0:
                somaNegativa += i
        return somaNegativa
    print("Soma Elementos Negativos:", somaNegativa(lista))

    # G
    def vizinhosIguais(lista):
        vizinhosSalvos = []
        vizinhosIguais = 0
        for i in range(len(lista)):
            frente = i + 1
            atras = i - 1

            if i not in vizinhosSalvos:
                if frente <= len(lista) - 1:
                    if lista[i] == lista[frente]:
                        vizinhosIguais += 1
                        vizinhosSalvos.append(lista[i])

                if atras >= 0:
                    if lista[i] == lista[atras]:
                        vizinhosIguais += 1
                        vizinhosSalvos.append(lista[i])
        return vizinhosIguais
    print("Quantidade de Vizinhos Iguais:", vizinhosIguais(lista))

formatadorLista(int(input("Quantidade de números: ")))
