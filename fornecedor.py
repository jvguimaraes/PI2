lista_fornecedores = [['beto farias', 'tecnologia',
                       'betofarias@gmail.com', '990066551', '00011122233']]


def cadastro_fornecedor():

    # lista com todos os dados do fornecedor
    fornecedor = []

    # lista com os produtos que o fornecedores criar
    lista_produtos = []

    fornecedor_nome = ""
    espaco = " "
    ja_existe_nome = False

    fornecedor_area = ""

    fornecedor_email = ""
    arroba = "@"
    pontocom = ".com"
    ja_existe_email = False

    fornecedor_telefone = ""
    ja_existe_telefone = False

    fornecedor_cpf = ""
    ja_existe_cpf = False

    # verifica se o nome não esta em branco
    while (len(fornecedor_nome) < 3) or (espaco not in fornecedor_nome) or (ja_existe_nome == True):
        fornecedor_nome = input("digite seu nome completo(nome e sobrenome): ")
        if (len(fornecedor_nome) < 3) or (espaco not in fornecedor_nome):
            print("digite nome e sobrenome separados por espaço")

        # verifica se o nome ja foi cadastrado
        tamanho = len(lista_fornecedores)

        for i in range(tamanho):
            if (lista_fornecedores[i][0]) == fornecedor_nome:
                print(f"{fornecedor_nome}, nome ja cadastrado")
                ja_existe_nome = True
            else:
                ja_existe_nome = False

    # verifica se a area de atuação não esta em branco
    while len(fornecedor_area) < 2:
        fornecedor_area = input("qual sua area de atuação: ")
        if (len(fornecedor_area)) < 2:
            print("nome muito curto, tente denovo")

    # verifica se o email é valido
    while (len(fornecedor_email) < 6) or (arroba not in fornecedor_email or pontocom not in fornecedor_email) or (ja_existe_email == True):

        fornecedor_email = input("digite o seu email: ")
        if (len(fornecedor_email) < 6) or (arroba not in fornecedor_email or pontocom not in fornecedor_email):
            print("email invalido, digite um email valido")

        # verifica se o email ja foi cadastrado
        tamanho = len(lista_fornecedores)

        for i in range(tamanho):
            if (lista_fornecedores[i][2]) == fornecedor_email:
                print(f"{fornecedor_email}, email ja cadastrado")
                ja_existe_email = True
            else:
                ja_existe_email = False

    # verifica se o numero tem pelo menos 9 digitos, se não pede novamente
    while (len(fornecedor_telefone) < 9) or (ja_existe_telefone == True):
        fornecedor_telefone = input("digite o seu telefone: ")
        if len(fornecedor_telefone) < 9:
            print("numero incompleto, pelo menos 9 digitos")

        # verifica se o telefone ja foi cadastrado
        tamanho = len(lista_fornecedores)

        for i in range(tamanho):
            if (lista_fornecedores[i][3]) == fornecedor_telefone:
                print(f"{fornecedor_telefone}, telefone ja cadastrado")
                ja_existe_telefone = True
            else:
                ja_existe_telefone = False

    # verifica se o cpf tem o numero certo de digitos, se não pede cpf novamente
    while (len(fornecedor_cpf) != 11) or (ja_existe_cpf == True):
        fornecedor_cpf = input("digite o seu CPF/CNPJ: ")
        if len(fornecedor_cpf) != 11:
            print("cpf não valido")

        # verifica se o cpf ja foi cadastrado
        tamanho = len(lista_fornecedores)

        for i in range(tamanho):
            if (lista_fornecedores[i][4]) == fornecedor_cpf:
                print(f"{fornecedor_cpf}, cpf ja cadastrado")
                ja_existe_cpf = True
            else:
                ja_existe_cpf = False

    # adiciona todos os itens na lista do fornecedor
    fornecedor.append(fornecedor_nome)
    fornecedor.append(fornecedor_area)
    fornecedor.append(fornecedor_email)
    fornecedor.append(fornecedor_telefone)
    fornecedor.append(fornecedor_cpf)

    # adiciona a lista do fornecedor a lista de fornecedores
    lista_fornecedores.append(fornecedor)
    print("cadastro realizado com sucesso!")
    # print(lista_fornecedores)


def main():
    while True:
        menu = input("oque deseja fazer? \n 1-cadastrar fronecedor")

        if menu == "1":
            cadastro_fornecedor()


if __name__ == "__main__":
    main()
