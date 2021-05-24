# Teste
def serieRecursiva(n):
    n1 = n + 1
    n2 = n + 2

    if n == 0 or n2 == 0:
        return 0

    print(str(n1) + " / " + str(n2) + " = ", n1 / n2)

    return n1 / n2 + serieRecursiva(n - 1)

def serie(n):
    n1, n2 = 1, 1
    soma = 0

    for i in range(n):
        soma += n1 / n2
        print(str(i + 1) + " -> " + str(n1) + " / " + str(n2) + " = ", n1 / n2)

        n1, n2 = n1 + 1, n2 + 2

    return soma


def main():
    print("Série de 9: ", serie(9))


main()
