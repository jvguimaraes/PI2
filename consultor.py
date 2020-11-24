consultores = []


def cadastro_consultor():
    dados = dict()
    dados['nome'] = input('Nome: ')
    dados['área_de_atuação'] = input('Área de Atuação: ')
    dados['email'] = input('E-mail: ')
    dados['telefone'] = input('Telefone: ')
    dados['cnpj/cpf'] = input('CNPJ/CPF: ')
    dados['lista_de_especialidades'] = input('Lista de Especialidades: ')
    consultores.append(dados)
    # print(dados)
