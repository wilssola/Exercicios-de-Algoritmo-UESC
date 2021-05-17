def incluirNovoNome(db):
    nome = input('Nome do Usuário: ')

    if nome in db:
        print('Usuário já existente')
    else:
        try:
            db[nome] = {'telefones': []}
            print('Usuário adicionado com Sucesso')

            while True:
                acao = input(
                    'Deseja adicionar Telefones para esse Usuário? (y/n) ')
                if acao.lower() == 'y':
                    incluirTelefone(db, nome)
                    break
                elif acao.lower() == 'n':
                    break
        except:
            print('Erro ao adicionar Usuário')


def incluirTelefone(db, nome=''):
    if len(nome) <= 0:
        nome = input('Digite o nome do Usuário: ')

    while True:
        if nome in db.keys():
            quantidade = int(input('Quantos Telefones deseja adicionar? '))

            for i in range(quantidade):
                while True:
                    try:
                        numero = int(input('Telefone ' + str(i + 1) + ': '))

                        try:
                            db[nome]['telefones'].append(numero)
                            print('Telefone adicionado com Sucesso')
                        except:
                            print('Erro ao adicionar Telefone')

                        break
                    except:
                        print('Telefone inválido')
            break
        else:
            print('Usuário inválido')
            nome = input('Digite o nome do Usuário: ')


def excluirNome(db, nome=''):
    if len(nome) <= 0:
        nome = input('Digite o nome do Usuário: ')

    while True:
        if nome in db.keys():
            try:
                del db[nome]
                print('Usuário deletado com Sucesso')
            except:
                print('Erro ao deletar Usuário')
            break
        else:
            print('Usuário inválido')
            nome = input('Digite o nome do Usuário: ')


def excluirTelefone(db, nome=''):
    if len(nome) <= 0:
        nome = input('Digite o nome do Usuário: ')

    while True:
        if nome in db.keys():
            while True:
                try:
                    consultarTelefone(db, nome)
                    telefone = int(
                        input('Digite o ID do Telefone que deseja remover: '))

                    try:
                        del db[nome]['telefones'][telefone - 1]
                        print('Telefone deletado com Sucesso')
                    except:
                        print('Erro ao deletar Telefone')

                    break
                except:
                    print('ID inválido')
            break
        else:
            print('Usuário inválido')
            nome = input('Digite o nome do Usuário: ')


def consultarTelefone(db, nome=''):
    if len(nome) <= 0:
        nome = input('Digite o nome do Usuário: ')

    while True:
        if nome in db.keys():
            print('\nLista de Telefones - Usuário', nome)

            for i in range(len(db[nome]['telefones'])):
                print('Telefone ' + str(i + 1) + ' - ' +
                      str(db[nome]['telefones'][i]))

            break
        else:
            print('Usuário inválido')
            nome = input('Digite o nome do Usuário: ')


def main():
    db = {}

    print('SISTEMA DE AGENDA TELEFÔNICA')
    while True:
        try:
            print('\nUse Ctrl+C para cancelar Ações')
            acao = int(input(
                'Digite 0 para sair, 1 para incluirNovoNome, 2 para incluirTelefone, 3 para excluirNome, 4 para excluirTelefone ou 5 para consultarTelefone: '))
            if acao == 0:
                print('\nPROGRAMA ENCERRADO')
                break
            elif acao == 1:
                incluirNovoNome(db)
            elif acao == 2:
                incluirTelefone(db)
            elif acao == 3:
                excluirNome(db)
            elif acao == 4:
                excluirTelefone(db)
            elif acao == 5:
                consultarTelefone(db)
            else:
                print('Função desconhecida')
        except (KeyboardInterrupt):
            print('\nAção cancelada')

    print('\nDB:')
    print(db)


main()
