produtosCount = 0
produtos = []
PROD_ID = 0
PROD_NOME = 1
PROD_DESC = 2
PROD_VALUE = 3
PROD_CAT = 4
PROD_FORNEC = 5


def salvaProduto(id, produto):
    arq = open("produtos.txt", 'a+')
    for item in produto:
        arq.write("{0}\n".format(item))
    arq.close()


def leProduto(id):
    arq = open("produtos.txt", 'r+')
    while True:
        nid = arq.readline().rstrip("\n")
        if (nid == ""):
            return None
        nome = arq.readline().rstrip("\n")
        descricao = arq.readline().rstrip("\n")
        valor = arq.readline().rstrip("\n")
        categoria = arq.readline().rstrip("\n")
        fornecedor = arq.readline().rstrip("\n")
        if (int(nid) == id):
            return [id, nome, descricao, valor, categoria, fornecedor]


def carregaProdutos():
    global produtosCount
    global produtos

    arq = open("produtos.txt", 'a+')
    arq.seek(0)
    while True:
        nid = arq.readline().rstrip("\n")
        if (nid == ""):
            arq.close()
            return
        nome = arq.readline().rstrip("\n")
        descricao = arq.readline().rstrip("\n")
        valor = arq.readline().rstrip("\n")
        categoria = arq.readline().rstrip("\n")
        fornecedor = arq.readline().rstrip("\n")

        produtos.append([int(nid),
                         nome,
                         descricao,
                         valor,
                         categoria,
                         fornecedor])
        produtosCount += 1


def cadastraProduto():
    global produtosCount
    produto = []
    print("Insira os dados do produto:")
    produto.append(produtosCount)
    produto.append(input("Nome: "))
    produto.append(input("Descrição: "))
    produto.append(int(input("Valor: ")))
    produto.append(input("Categoria: "))
    produto.append(input("Fornecedor: "))
    salvaProduto(produtosCount, produto)
    produtosCount += 1
    produtos.append(produto)
    print("cadastro realizado com sucesso!")


def imprimeProduto(produto):
    print("Produto:")
    print("\tid = {0}".format(produto[PROD_ID]))
    print("\tnome = {0}".format(produto[PROD_NOME]))
    print("\tdescricao = {0}".format(produto[PROD_DESC]))
    print("\tvalor = {0}".format(produto[PROD_VALUE]))
    print("\tcategoria = {0}".format(produto[PROD_CAT]))
    print("\tfornecedor = {0}".format(produto[PROD_FORNEC]))


def pesquisa(index, param):
    global produtos
    results = []
    for produto in produtos:
        if param.lower() in produto[index].lower():
            results.append(produto)
    return results


def pesquisaPorNome(nome):
    return pesquisa(PROD_NOME, nome)


def pesquisaPorCategoria(categoria):
    return pesquisa(PROD_CAT, categoria)


def pesquisaPorFornecedor(fornecedor):
    return pesquisa(PROD_FORNEC, fornecedor)


if __name__ == "__main__":
    carregaProdutos()
    for produto in produtos:
        imprimeProduto(produto)
    cadastraProduto()
    for produto in produtos:
        imprimeProduto(produto)
