import produto
import fornecedor
import consultor
import necessidade


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
        pass
    elif opcao == 3:
        consultor.cadastro_consultor()
    elif opcao == 4:
        produto.cadastraProduto()
    elif opcao == 5:
        necessidade.cadastro_necessidade()
    elif opcao == 6:
        pass
    else:
        return


def menuPesquisaExecuta(opcao):
    if opcao == 1:
        pass
    elif opcao == 2:
        pass
    elif opcao == 3:
        pass
    elif opcao == 4:
        pass
    else:
        return


def main():
    iniciaMenu(imprimeMenuPrincipal, menuPrincipalExecuta)


if __name__ == "__main__":
    main()
