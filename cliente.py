clientes = []


def cadastro_cliente():
    dados = dict()
    dados['nome'] = input('Nome: ')
    dados['área_de_atuação'] = input('Área de Atuação: ')
    dados['email'] = input('E-mail: ')
    dados['telefone'] = input('Telefone: ')
    dados['cnpj/cpf'] = input('CNPJ/CPF: ')
    dados['necessidades'] = input('Lista de necessidades: ')
    clientes.append(dados)
    # print(dados)


def pesquisa_cliente_nome():
    pesquisa = input("digite a sua pesquisa: ")
    lista_pesquisa = []

    tamanho = len(clientes)

    for i in range(tamanho):
        if pesquisa in (clientes[i]['nome']):
            lista_pesquisa.append(clientes[i]['nome'])

    print(f"foram encontrados os seguintes clientes: \n {lista_pesquisa}")


def pesquisa_cliente_necessidade():
    pesquisa = input("digite a sua pesquisa: ")
    lista_pesquisa = []

    tamanho = len(clientes)

    for i in range(tamanho):
        if pesquisa in (clientes[i]['necessidades']):
            lista_pesquisa.append(clientes[i]['nome'])

    print(f"foram encontrados os seguintes clientes: \n {lista_pesquisa}")


def pesquisa_cliente_area():
    pesquisa = input("digite a sua pesquisa: ")
    lista_pesquisa = []

    tamanho = len(clientes)

    for i in range(tamanho):
        if pesquisa in (clientes[i]['área_de_atuação']):
            lista_pesquisa.append(clientes[i]['nome'])

    print(f"foram encontrados os seguintes clientes: \n {lista_pesquisa}")


def main():
    print('CADASTRO DE CLIENTE\n')
    cadastro_cliente()


if __name__ == "__main__":
    main()
