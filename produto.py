count = 0

def salvaProduto(id, produto):
    arq = open("[{0}].product".format(id), 'w')
    for item in produto:
        arq.write("{0}\n".format(item))
    arq.close()


def leProduto(id):
    arq = open("[{0}].product".format(id), 'r')
    id = arq.readline().rstrip("\n")
    nome = arq.readline().rstrip("\n")
    descricao = arq.readline().rstrip("\n")
    valor = arq.readline().rstrip("\n")
    categoria = arq.readline().rstrip("\n")
    fornecedor = arq.readline().rstrip("\n")
    return [id, nome, descricao, valor, categoria, fornecedor]


def cadastraProduto():
    global count
    produto = []
    print("Insira os dados do produto:")
    produto.append(count)
    produto.append(input("Nome: "))
    produto.append(input("Descrição: "))
    produto.append(int(input("Valor: ")))
    produto.append(input("Categoria: "))
    produto.append(input("Fornecedor: "))
    salvaProduto(count, produto)
    count += 1


def imprimeProduto(produto):
    print("Produto:")
    print("\tid = {0}".format(produto[0]))
    print("\tnome = {0}".format(produto[1]))
    print("\tdescricao = {0}".format(produto[2]))
    print("\tvalor = {0}".format(produto[3]))
    print("\tcategoria = {0}".format(produto[4]))
    print("\tfornecedor = {0}".format(produto[5]))

if __name__ == "__main__":
    cadastraProduto()
    produto = leProduto(0)
    imprimeProduto(produto)


    