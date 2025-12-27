# Mini sistema de cadastro
# Projeto iniciante em Python

pessoas = []  # lista para armazenar os cadastros

opcao = 0

while opcao != 3:
    print("\nMenu")
    print("1 - Cadastrar pessoa")
    print("2 - Listar pessoas cadastradas")
    print("3 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        # Cadastro
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))

        pessoa = {
            "nome": nome,
            "idade": idade
        }

        pessoas.append(pessoa)
        print("Pessoa cadastrada com sucesso!")

    elif opcao == 2:
        # Listagem
        if len(pessoas) == 0:
            print("Nenhuma pessoa cadastrada.")
        else:
            print("\nPessoas cadastradas:")
            for i, pessoa in enumerate(pessoas, start=1):
                print(f"{i} - {pessoa['nome']} | {pessoa['idade']} anos")

    elif opcao == 3:
        print("Saindo do sistema...")

    else:
        print("Opção inválida!")
