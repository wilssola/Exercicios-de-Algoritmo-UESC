def conta_vogais(texto):
    kVogais = ["a", "e", "i", "o", "u"]

    if len(texto) <= 0:
        return 0

    if texto[-1].lower() in kVogais:
        return conta_vogais(texto[0:len(texto)-1]) + 1

    return conta_vogais(texto[0:len(texto)-1])


def main():
    textos = ["aeiou", "Irineu", "Hello, World!"]

    for texto in textos:
        print("\nTexto:", texto)
        print("Quantidade de Vogais:", conta_vogais(texto))


main()
