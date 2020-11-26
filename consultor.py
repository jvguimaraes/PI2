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


def pesquisa_consultor():
    pesquisa = input("digite a sua pesquisa: ")
    lista_pesquisa = []

    tamanho = len(consultores)

    for i in range(tamanho):
        if pesquisa in (consultores[i]['lista_de_especialidades']):
            lista_pesquisa.append(consultores[i]['nome'])

    print(f"foram encontrados os seguintes consultores com essa especialidade: \n {lista_pesquisa}")

