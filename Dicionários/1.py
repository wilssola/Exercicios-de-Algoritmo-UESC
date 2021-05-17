def inputFloat(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print('Valor inválido')


def calcularMelhorVolta(db):
    melhorVolta = 0
    melhorTempo = 0
    melhorCorredor = ''
    for corredor in db:
        for volta in db[corredor]['voltas']:
            if db[corredor]['voltas'][volta] < melhorTempo or melhorTempo == 0:
                melhorVolta = volta
                melhorTempo = db[corredor]['voltas'][volta]
                melhorCorredor = corredor

    return (melhorVolta, melhorTempo, melhorCorredor)


def calcularColocacao(db):
    colocacao = []
    for corredor in db:
        if 'media' in db[corredor].keys():
            colocacao.append((db[corredor]['media'], corredor))
    colocacao.sort()
    return colocacao


def main():
    kCorredores = 6
    kVoltas = 10

    db = {}

    print('SISTEMA PARA CORRIDA DE KART')

    try:
        for i in range(kCorredores):
            while True:
                nome = input('\nCorredor ' + str(i + 1) + ' - Nome: ')
                if len(nome) > 0:
                    break
                print('Nome inválido')

            db[nome] = {'voltas': {}}
            somaVoltas = 0
            for j in range(kVoltas):
                segundos = inputFloat('Corredor ' + str(i + 1) +
                                      ' - Volta ' + str(j + 1) + ' - Tempo (segundos): ')
                somaVoltas += segundos
                db[nome]['voltas'][j + 1] = segundos
            db[nome]['media'] = somaVoltas / kVoltas
    except (KeyboardInterrupt):
        print('\n\nPROGRAMA ENCERRADO')

    melhorVolta = calcularMelhorVolta(db)
    if len(melhorVolta[-1]) > 0:
        print('\nMELHOR VOLTA:')
        print('A melhor volta foi a Volta', str(
            melhorVolta[0]) + ',', 'com o Tempo de', melhorVolta[1], 'segundos, do Corredor', melhorVolta[2])

    colocacao = calcularColocacao(db)
    if len(colocacao) > 0:
        print('\nCOLOCAÇÃO:')
        for i in range(len(colocacao)):
            print(str(i + 1) + '° - Corredor:',
                  colocacao[i][1], '- Média de Tempo:', colocacao[i][0], 'segundos')

    print('\nDB:')
    print(db)


main()
