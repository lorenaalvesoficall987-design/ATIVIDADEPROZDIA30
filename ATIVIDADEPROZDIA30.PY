
produtos = []


def cadastrar_produto():
    print("\n--- CADASTRAR PRODUTO ---")

    codigo = input("Digite o código do produto: ")

    for item in produtos:
        if item["codigo"] == codigo:
            print("Já existe um produto com esse código!")
            return

    nome = input("Digite o nome do produto: ")

    try:
        preco = float(input("Digite o preço do produto: R$ "))
        estoque = int(input("Digite a quantidade em estoque: "))

        if preco < 0 or estoque < 0:
            print("O preço e o estoque não podem ser negativos.")
            return

    except ValueError:
        print("Erro! Digite um preço e uma quantidade válidos.")
        return

    produto = {
        "codigo": codigo,
        "nome": nome,
        "preco": preco,
        "estoque": estoque
    }

    produtos.append(produto)
    print("Produto cadastrado com sucesso!")


def listar_produto():
    print("\n--- LISTA DE PRODUTOS ---")

    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
    else:
        for item in produtos:
            print("-------------------------")
            print("Código:", item["codigo"])
            print("Nome:", item["nome"])
            print("Preço: R$", round(item["preco"], 2))
            print("Estoque:", item["estoque"])


def pesquisar_produto():
    print("\n--- PESQUISAR PRODUTO ---")

    busca = input("Digite o nome ou código do produto: ").lower()
    encontrado = False

    for item in produtos:
        if busca in item["nome"].lower() or busca == item["codigo"].lower():
            print("-------------------------")
            print("Código:", item["codigo"])
            print("Nome:", item["nome"])
            print("Preço: R$", round(item["preco"], 2))
            print("Estoque:", item["estoque"])
            encontrado = True

    if encontrado == False:
        print("Produto não encontrado.")


def consultar_estoque():
    print("\n--- CONSULTAR ESTOQUE ---")

    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
    else:
        for item in produtos:
            print(
                item["nome"],
                "- Quantidade:",
                item["estoque"]
            )

            if item["estoque"] <= 5:
                print("Atenção: estoque baixo!")


def registrar_venda():
    print("\n--- REGISTRAR VENDA ---")

    codigo = input("Digite o código do produto: ")

    for item in produtos:
        if item["codigo"] == codigo:
            try:
                quantidade = int(input("Quantidade vendida: "))
            except ValueError:
                print("Digite uma quantidade válida.")
                return

            if quantidade <= 0:
                print("Digite uma quantidade maior que zero.")

            elif quantidade <= item["estoque"]:
                total = quantidade * item["preco"]
                item["estoque"] -= quantidade

                print("Venda realizada com sucesso!")
                print("Valor total: R$", round(total, 2))
                print("Estoque restante:", item["estoque"])

            else:
                print("Estoque insuficiente!")

            return

    print("Produto não encontrado.")


def menu():
    print("\n==============================")
    print("   SISTEMA DE LOJA DE ROUPAS")
    print("==============================")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Pesquisar produto")
    print("4 - Consultar estoque")
    print("5 - Registrar venda")
    print("6 - Sair")
    print("==============================")


while True:
    menu()

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_produto()

    elif opcao == "2":
        listar_produto()

    elif opcao == "3":
        pesquisar_produto()

    elif opcao == "4":
        consultar_estoque()

    elif opcao == "5":
        registrar_venda()

    elif opcao == "6":
        print("Sistema encerrado. Obrigada!")
        break

    else:
        print("Opção inválida! Tente novamente.")
