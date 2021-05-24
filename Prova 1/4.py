def intercalarListas(lista1, lista2):
    if len(lista1) == 0:
        return lista2
    if len(lista2) == 0:
        return lista1
    if len(lista1) == 0 and len(lista2) == 0:
        return []

    if len(lista1) == 1 or len(lista2) == 1:
        return lista1 + lista2

    return [lista1[0]] + [lista2[0]] + intercalarListas(lista1[1:], lista2[1:])


def main():
    lista1 = ["aeiou", "Irineu", "Hello, World!"]
    lista2 = ["abcdefghijklmnopqrstuvwxyz", "Jairo", "Bye, World!"]

    print("lista1:", lista1)
    print("lista2:", lista2)

    print("\nintercalarListas(lista1, lista2):", intercalarListas(lista1, lista2))

main()
