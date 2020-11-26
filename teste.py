import produto
import fornecedor
import consultor
import necessidade
import especialidade
import cliente


def imprimeMenuPrincipal():
    print("SOFTWHERE\n")
    print("\tMenu")
    print("\t01 - Cadastro")
    print("\t02 - Pesquisa")
    print("\t99 - Sair")


def imprimeMenuCadastro():
    print("SOFTWHERE\n")
    print("\tMenu Cadastro")
    print("\t01 - Fornecedor")
    print("\t02 - Cliente")
    print("\t03 - Consultor")
    print("\t04 - Produto")
    print("\t05 - Necessidade")
    print("\t06 - Especialidade")
    print("\t99 - Voltar")


def imprimeMenuPesquisa():
    print("SOFTWHERE\n")
    print("\tMenu Pesquisa")
    print("\t01 - Produto")
    print("\t02 - Cliente")
    print("\t03 - Consultor")
    print("\t99 - Voltar")


def imprimeMenuPesquisaProduto():
    print("SOFTWHERE\n")
    print("\tMenu Pesquisa Produto")
    print("\t01 - Por Nome")
    print("\t02 - Por Categoria")
    print("\t03 - Por Fornecedor")
    print("\t99 - Voltar")


def imprimeMenuPesquisaCliente():
    print("SOFTWHERE\n")
    print("\tMenu Pesquisa Produto")
    print("\t01 - Por Nome")
    print("\t02 - Por Área de Atuação")
    print("\t03 - Por Necessidade")
    print("\t99 - Voltar")


def imprimeMenuPesquisaConsultor():
    print("SOFTWHERE\n")
    print("\tMenu Pesquisa Produto")
    print("\t01 - Por Especialidade")
    print("\t99 - Voltar")


def iniciaMenu(funcaoImprimeOpcoes, funcaoExecuta):
    opcao = 0
    while opcao != 99:
        funcaoImprimeOpcoes()
        opcao = int(input("\tOpcao: "))
        if opcao != 99:
            funcaoExecuta(opcao)


def menuPrincipalExecuta(opcao):
    if opcao == 1:
        iniciaMenu(imprimeMenuCadastro, menuCadastroExecuta)
    elif opcao == 2:
        iniciaMenu(imprimeMenuPesquisa, menuPesquisaExecuta)
    else:
        return


def menuCadastroExecuta(opcao):
    if opcao == 1:
        fornecedor.cadastro_fornecedor()
    elif opcao == 2:
        cliente.cadastro_cliente()
    elif opcao == 3:
        consultor.cadastro_consultor()
    elif opcao == 4:
        produto.cadastraProduto()
    elif opcao == 5:
        necessidade.cadastro_necessidade()
    elif opcao == 6:
        especialidade.cadastro_especialidade()
    else:
        return


def menuPesquisaExecuta(opcao):
    if opcao == 1:
        iniciaMenu(imprimeMenuPesquisaProduto, menuPesquisaProdutoExecuta)
    elif opcao == 2:
        pass
    elif opcao == 3:
        pass
    elif opcao == 4:
        pass
    else:
        return


def menuPesquisaProdutoExecuta(opcao):
    resultadoPesquisa = []
    if opcao == 1:
        nome = input("Nome: ")
        resultadoPesquisa = produto.pesquisaPorNome(nome)
    elif opcao == 2:
        categoria = input("Categoria: ")
        resultadoPesquisa = produto.pesquisaPorCategoria(categoria)
    elif opcao == 3:
        fornecedor = input("Fornecedor: ")
        resultadoPesquisa = produto.pesquisaPorFornecedor(fornecedor)
    else:
        return

    for item in resultadoPesquisa:
        produto.imprimeProduto(item)
    if len(resultadoPesquisa) == 0:
        print("Nenhum resultado encontrado!")


def menuPesquisaClienteExecuta(opcao):
    if opcao == 1:
        cliente.pesquisa_cliente()
    elif opcao == 2:
        cliente.pesquisa_area_atuacao()
    elif opcao == 3:
        cliente.pesquisa_necessidade()
    else:
        return


def init():
    produto.carregaProdutos()


def main():
    init()
    iniciaMenu(imprimeMenuPrincipal, menuPrincipalExecuta)


if __name__ == "__main__":
    main()
