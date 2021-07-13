import json


class Agenda():
    def _init_(self, nome='', telefone=''):
        self.nome = nome
        self.telefone = telefone

    def fromJson(self, jsonString):
        dicionario = json.loads(jsonString)

        self.nome = dicionario['nome']
        self.telefone = dicionario['telefone']

        return self

    def toJson(self):
        dicionario = {'nome': self.nome,
                      'telefone': self.telefone, }

        return json.dumps(dicionario)

def adicionarTelefones(lista=[]):
    if len(lista) == 0:
        lista = lerTelefones()
        
    kListaSim = ['y', 'yes', 's', 'sim']

    if input('Deseja inserir os valores de teste? ') not in kListaSim:
        while True:
            nome = input('Nome: ')
            telefone = input('Telefone: ')

            agenda = Agenda()
            agenda.nome = nome
            agenda.telefone = telefone
            lista.append(agenda)

            if input('Deseja adicionar mais um? ') not in kListaSim:
                break
    else:
        listaTeste = [['Paulo', '2345-2354'], ['André', '9956-6644'], ['Ana', '98823-2323']]
        for teste in listaTeste:
            nome = teste[0]
            telefone = teste[1]

            agenda = Agenda()
            agenda.nome = nome
            agenda.telefone = telefone
            lista.append(agenda)

    salvarTelefones(lista)

def listarTelefones(lista=[]):
    if len(lista) == 0:
        lista = lerTelefones()

    novaLista = []

    for agenda in lista:
        novaLista.append([agenda.nome, agenda.telefone])

    return novaLista

def salvarTelefones(lista):
    arquivoJson = open('telefones.json', 'w')

    listaJson = []

    for agendaClass in lista:
        listaJson.append(agendaClass.toJson())

    json.dump(listaJson, arquivoJson)

def lerTelefones():
    try:
        arquivoJson = open('telefones.json', 'r')

        listaJson = json.load(arquivoJson)
        listaClass = []

        for agendaJson in listaJson:
            agendaClass = Agenda().fromJson(agendaJson)
            listaClass.append(agendaClass)

        return listaClass
    except:
        arquivoJson = open('telefones.json', 'w')

        listaJson = []

        json.dump(listaJson, arquivoJson)

        return listaJson

def main():
    while True:
        telefones = lerTelefones()
        opcao = int(input(
            'Escolha uma função: (1 - Adicionar telefone, 2 - Listar telefones, 0 - Fechar programa) '))
        if opcao == 1:
            adicionarTelefones(telefones)
        elif opcao == 2:
            print(listarTelefones(telefones))
        elif opcao == 0:
            print('Programa encerrado')
            break
        else:
            print('Função desconhecida')

main()
