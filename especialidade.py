especialidades = []


def cadastro_especialidade():
    dados = dict()
    dados['nome'] = input('Nome: ')
    dados['descrição'] = input('Descrição: ')
    dados['ID'] = input('ID: ')
    dados['categoria'] = input('Caregoria: ')
    dados['consultor'] = input('Consultor: ')

    especialidades.append(dados)
    # print(dados)
