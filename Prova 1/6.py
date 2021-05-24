def verificadorParInverso(palavra1, palavra2):
    if palavra1[::-1].lower() == palavra2.lower():
        return True

    return False


def main():
    textos1 = ["aeiou", "Irineu", "Hello, World!"]
    textos2 = ["uoiea", "Ueniri", "Hello, World!"]

    for texto1 in textos1:
        for texto2 in textos2:
            print("\nTexto1:", texto1)
            print("Texto2:", texto2)
            print("Par Inverso:", verificadorParInverso(texto1, texto2))


main()
