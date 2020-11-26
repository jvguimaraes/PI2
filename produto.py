produtosCount = 0
produtos = []
PROD_ID = 0
PROD_NOME = 1
PROD_DESC = 2
PROD_VALUE = 3
PROD_CAT = 4
PROD_FORNEC = 5


def salvaProduto(id, produto):
    arq = open("[{0}].product".format(id), 'w')
    for item in produto:
        arq.write("{0}\n".format(item))
    arq.close()


def leProduto(id):
    arq = open("[{0}].product".format(id), 'r')
    arq.readline().rstrip("\n")
    nome = arq.readline().rstrip("\n")
    descricao = arq.readline().rstrip("\n")
    valor = arq.readline().rstrip("\n")
    categoria = arq.readline().rstrip("\n")
    fornecedor = arq.readline().rstrip("\n")
    return [id, nome, descricao, valor, categoria, fornecedor]


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
        if param in produto[index]:
            results.append(produto)
    return results


def pesquisaPorNome(nome):
    return pesquisa(PROD_NOME, nome)


def pesquisaPorCategoria(categoria):
    return pesquisa(PROD_CAT, categoria)


def pesquisaPorFornecedor(fornecedor):
    return pesquisa(PROD_FORNEC, fornecedor)


if __name__ == "__main__":
    cadastraProduto()
    produto = leProduto(0)
    imprimeProduto(produto)
