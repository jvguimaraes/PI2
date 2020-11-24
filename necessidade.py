necessidades = []


def cadastro_necessidade():
    # Coleta as informações da necessidade
    cliente = input('Qual o nome da empresa? ')
    necessidade = input('Você precisa de um software para: ')
    descricao = input('Faça uma breve descrição da sua necessidade: ')
    categoria = input('Qual a categoria do software? ')
    identificacao = input('Insira uma identificação para este cadastro: ')

    # Imprime a revisão do cadastro
    print('\n Por favor, revise o seu cadastro.\n',
          'Nome da empresa: ' + cliente + '.\n',
          'Necessidade: ' + necessidade + '.\n',
          'Descrição: ' + descricao + '.\n', 'Categoria: ' + categoria + '.\n',
          'ID: ' + identificacao)

    confirmacao_cadastro()

    necessidades.append([cliente,
                         necessidade,
                         descricao,
                         categoria,
                         identificacao])

    # Cria arquivo .txt para armazenar variável necessidade
    arquivo = open('dados_necessidade.txt', 'a+')
    linhas = list()
    linhas.append(necessidade + '\n')
    arquivo.writelines(linhas)
    arquivo.close()

    # Cria arquivo .txt para armazenar variável categoria
    arquivo = open('dados_categoria.txt', 'a+')
    linhas = list()
    linhas.append(categoria + '\n')
    arquivo.writelines(linhas)
    arquivo.close()


def confirmacao_cadastro():
    cadastro = input(
        '\nSeu cadastro está correto?\nDigite 1 para NÃO ou 2 para SIM \n')
    cadastro = int(cadastro)

    if cadastro == 1:
        print('\nPor favor, preencha novamente seus dados: ')
        cadastro_necessidade()

    if cadastro == 2:
        print('Cadastro efetuado com sucesso!')

    else:
        print('\nOpção inválida.')
        confirmacao_cadastro()


def main():
    print('CADASTRO DE NECESSIDADE\n')
    cadastro_necessidade()
    confirmacao_cadastro()


if __name__ == "__main__":
    main()
