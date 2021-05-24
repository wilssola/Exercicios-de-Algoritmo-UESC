def main():
    kMeses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
              "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    lengthMeses = len(kMeses)
    rangeMeses = range(lengthMeses)

    print("Insira a Temperatura Média dos Meses a seguir:")

    temperaturas = []
    somaAnual = 0

    for i in rangeMeses:
        while True:
            try:
                media = float(
                    input(str(i + 1) + " - " + kMeses[i] + " (°C): "))
                break
            except ValueError:
                print("Valor inválido")
        somaAnual += media
        temperaturas.append(media)

    mediaAnual = somaAnual / lengthMeses
    print("\nMédia Anual:", mediaAnual)

    print("\nTemperaturas Acima da Média Anual:")
    for i in rangeMeses:
        if temperaturas[i] > mediaAnual:
            print(str(i + 1) + " - " +
                  kMeses[i] + ": " + str(temperaturas[i]) + "°C")


main()
