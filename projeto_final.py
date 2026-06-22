class Livro:
    def __init__(self, codigo, titulo, autor, ano):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.status = "disponível"  # Todo livro começa disponível

#BUSCAR LIVRO no codigo todo
def buscar_por_codigo(biblioteca, codigo):
    for livro in biblioteca:
        if livro.codigo == codigo:
            return livro
    return None
# 1 CADASTRO SE TEM OU NÃO UM LIVRO
def cadastrar_livro(biblioteca):
    print("Cadastrar Livro ")
    codigo = input("Código: ")
    #se o livro ja existe
    if buscar_por_codigo(biblioteca, codigo):
        print("Erro: Já existe um livro cadastrado com este código!")
        return
    #cadastro
    titulo = input("Título: ")
    autor = input("Autor (apenas o primeiro): ")
    ano = input("Ano de publicação: ")

    novo_livro = Livro(codigo, titulo, autor, ano)
    biblioteca.append(novo_livro)
    print("Livro cadastrado com sucesso!")

# 2 Consulta de livro
def consultar_livro(biblioteca):
    print("Consultar Livro")
    print("1 Por código")
    print("2. Por autor")
    opcao = input("Escolha a forma de busca: ")
     #por ID é igual, por so ter 1
    if opcao == "1":
        codigo = input("Digite o código: ")
        livro = buscar_por_codigo(biblioteca, codigo)
        if livro:
            print("\n Código: " , livro.codigo, " | Título: " , livro.titulo, " | Autor: " ,livro.autor,  " | Ano: " , livro.ano, "| Status: ", livro.status,)
        else:
            print("Livro não encontrado")
    # autor tem mais de 1 
    if opcao == "2":
        autor = input("Digite o nome do autor: ")
        for livro in biblioteca:
            if autor in livro.autor:
                print("\n Código:", livro.codigo , "| Título: ", livro.titulo , "| Autor: " , livro.autor ,"| Ano: ", livro.ano ,"| Status:", livro.status,)  
    else:
        print("Opção inválida.")

# 3 alteração de livro
def alterar_dados(biblioteca):
    print("Alterar Dados do Livro")
    codigo = input("Digite o código do livro que deseja alterar: ")
    livro = buscar_por_codigo(biblioteca, codigo)

    if livro:
        print("Modificando o livro: " ,livro.titulo)
        livro.titulo = input("Novo Título ")
        livro.autor = input("Novo Autor ")
        livro.ano = input("Novo Ano" )
        print("Dados alterados com sucesso!")
    else:
        print("Livro não encontrado")

# 4 Remover livro
def remover_livro(biblioteca):
    print("Remover Livro")
    codigo = input("Digite o código do livro a ser removido: ")
    livro = buscar_por_codigo(biblioteca, codigo)

    if livro:
        biblioteca.remove(livro)
        print("Livro removido com sucesso!")
    else:
        print("Livro não encontrado")

# 5LISTAR livro
def listar_todos(biblioteca):
    lista_ordenada = list(biblioteca)
    n = len(lista_ordenada)
    for i in range(n):
        #Nessa parte da ordenação nao sabia como fazer 
        for j in range(0, n - i - 1):
            if lista_ordenada[j].titulo.lower() > lista_ordenada[j + 1].titulo.lower():
                # Troca os elementos de lugar
               lista_ordenada[j], lista_ordenada[j + 1] = lista_ordenada[j + 1], lista_ordenada[j]        
    #para exibir apenas Título e Ano
    for livro in lista_ordenada:
        print("Título: ",livro.titulo, livro.ano)

# 6 Realizar emprestimo
def realizar_emprestimo(biblioteca):
    print("Realizar Empréstimo")
    codigo = input("Digite o código do livro: ")
    livro = buscar_por_codigo(biblioteca, codigo)

    if livro:
        if livro.status == "disponível":
            livro.status = "emprestado"
            print("Empréstimo do livro ", livro.titulo ," realizado com sucesso!")
        else:
            print("Livro já emprestado")
    else:
        print("Livro não encontrado")

#7 Realizar devolucão
def realizar_devolucao(biblioteca):
    print("Realizar Devolução")
    codigo = input("Digite o código do livro: ")
    livro = buscar_por_codigo(biblioteca, codigo)

    if livro:
        if livro.status == "emprestado":
            livro.status = "disponível"
            print("Devolução do livro ",livro.titulo, "realizada com sucesso!")
        else:
            print("Este livro já está disponível no sistema.")
    else:
        print("Livro não encontrado")


def menu():
    #Lista dos livros com a função menu
    biblioteca = []

    while True:
        print("\n SISTEMA DE CONTROLE DE BIBLIOTECA")
        print("1. Cadastrar livro")
        print("2. Consultar livro")
        print("3. Alterar dados")
        print("4. Remover livro")
        print("5. Listar todos")
        print("6. Realizar empréstimo")
        print("7. Realizar devolução")
        print("8. Sair")
        
        opcao = input("Escolha uma opção (1-8): ")
        if opcao == "1":
            cadastrar_livro(biblioteca)
        else:
            if opcao == "2":
                consultar_livro(biblioteca)
            else:
                if opcao == "3":
                    alterar_dados(biblioteca)
                else:
                    if opcao == "4":
                        remover_livro(biblioteca)
                    else:
                        if opcao == "5":
                            listar_todos(biblioteca)
                        else:
                            if opcao == "6":
                                realizar_emprestimo(biblioteca)
                            else:
                                if opcao == "7":
                                    realizar_devolucao(biblioteca)
                                else:
                                    if opcao == "8":
                                        print("Finalizando o programa. Até logo!")
                                        return
                                    else:
                                        print("Opção inválida! Tente novamente.")
menu()
