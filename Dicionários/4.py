def incluirProduto(db):
    nome = input('Nome do Produto: ')

    if nome in db:
        print('Produto já existente')
    else:
        try:
            db[nome] = {'preco': 0}
            print('Produto adicionado com Sucesso')

            while True:
                acao = input(
                    'Deseja definir agora o Preço para esse Produto? (y/n) ')
                if acao.lower() == 'y':
                    incluirPreco(db, nome)
                    break
                elif acao.lower() == 'n':
                    break
        except:
            print('Erro ao adicionar Produto')


def incluirPreco(db, nome=''):
    if len(nome) <= 0:
        nome = input('Digite o nome do Produto: ')

    while True:
        if nome in db.keys():
            while True:
                try:
                    preco = float(input('Preço (R$): '))

                    try:
                        db[nome]['preco'] = preco
                        print('Preço adicionado com Sucesso')
                    except:
                        print('Erro ao adicionar Preço')

                    break
                except:
                    print('Preço inválido')
            break
        else:
            print('Produto inválido')
            nome = input('Digite o nome do Produto: ')


def excluirProduto(db, nome=''):
    if len(nome) <= 0:
        nome = input('Digite o nome do Produto: ')

    while True:
        if nome in db.keys():
            try:
                del db[nome]
                print('Produto deletado com Sucesso')
            except:
                print('Erro ao deletar Produto')
            break
        else:
            print('Produto inválido')
            nome = input('Digite o nome do Produto: ')


def consultarPreco(db, nome=''):
    if len(nome) <= 0:
        nome = input('Digite o nome do Produto: ')

    while True:
        if nome in db.keys():
            print('\nPreço do Produto', nome, '-',
                  "R$" + str(db[nome]['preco']))
            break
        else:
            print('Produto inválido')
            nome = input('Digite o nome do Produto: ')


def main():
    db = {'Salgado': {'preco': 4.5}, 'Lanche': {'preco': 6.5}, 'Suco': {
        'preco': 3}, 'Refrigerante': {'preco': 3.5}, 'Doce': {'preco': 1}}

    print('SISTEMA DE PRODUTOS E SEUS RESPECTIVOS PREÇOS')
    while True:
        try:
            print('\nUse Ctrl+C para cancelar Ações')
            acao = int(input(
                'Digite 0 para sair, 1 para incluirProduto, 2 para incluirPreco, 3 para excluirProduto ou 4 para consultarPreco: '))
            if acao == 0:
                print('\nPROGRAMA ENCERRADO')
                break
            elif acao == 1:
                incluirProduto(db)
            elif acao == 2:
                incluirPreco(db)
            elif acao == 3:
                excluirProduto(db)
            elif acao == 4:
                consultarPreco(db)
            else:
                print('Função desconhecida')
        except (KeyboardInterrupt):
            print('\nAção cancelada')

    print('\nDB:')
    print(db)


main()
