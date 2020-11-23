count = 0

def salvaProduto(id, produto):
    arq = open("[{0}].product".format(id), 'w')
    for item in produto:
        arq.write("{0}\n".format(item))
    arq.close()

def leProduto(id):
    arq = open("[{0}].product".format(id), 'r')
    id = arq.readline()
    nome = arq.readline()
    descricao = arq.readline()
    valor = arq.readline()
    categoria = arq.readline()
    fornecedor = arq.readline()
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

if __name__ == "__main__":
    cadastraProduto()

    