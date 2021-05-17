def contadorUnicosChar(string):
    dicionario = {}

    for i in range(len(string)):
        char = string[i].lower()
        if ord(char) >= 97 and ord(char) <= 122:
            dicionario[char] = 1

    soma = 0

    for i in dicionario:
        soma += dicionario[i]

    return soma


def main():
    aviso = 'Caracteres Únicos -'
    separador = '-'

    print(aviso, 'Hello, world!', separador,
          contadorUnicosChar('Hello, world!'))

    palavra = input('\nInsira uma palavra: ')
    print(aviso, palavra, separador, contadorUnicosChar(palavra))


main()
