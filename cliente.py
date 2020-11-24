clientes = []


def cadastro_cliente():
    nome_cliente = input('Qual o nome da empresa? ')
    area_atuacao = input('Qual sua área de atuação? ')
    email = input('Qual o Email? ')
    telefone = input('Qual o telefone? ')
    cnpj_cpf = input('Qual seu CNPJ/CPF? ')

    confirmacao_cadastro()

    clientes.append([nome_cliente,
                     area_atuacao,
                     email,
                     telefone,
                     cnpj_cpf])

    # Cria arquivo .txt para armazenar variável nome_cliente
    arquivo = open('dados_nome_cliente.txt', 'a+')
    linhas = list()
    linhas.append(nome_cliente + '\n')
    arquivo.writelines(linhas)
    arquivo.close()

    # Cria arquivo .txt para armazenar variável area_atuacao
    arquivo = open('dados_area_atuacao.txt', 'a+')
    linhas = list()
    linhas.append(area_atuacao + '\n')
    arquivo.writelines(linhas)
    arquivo.close()


def confirmacao_cadastro():
    cadastro = input(
        '\nSeu cadastro está correto?\nDigite 1 para NÃO ou 2 para SIM \n')
    cadastro = int(cadastro)

    if cadastro == 1:
        print('\nPor favor, preencha novamente seus dados: ')
        cadastro_cliente()

    if cadastro == 2:
        print('Cadastro efetuado com sucesso!')

    else:
        print('\nOpção inválida.')
        confirmacao_cadastro()


def main():
    print('CADASTRO DE CLIENTE\n')
    cadastro_cliente()
    confirmacao_cadastro()


if __name__ == "__main__":
    main()
