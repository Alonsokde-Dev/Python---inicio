# Menu simples usando while

opcao = 0

while opcao != 3:
    print("\nMenu")
    print("1 - Dizer Olá")
    print("2 - Mostrar um número")
    print("3 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("Olá! Bem-vindo ao sistema.")
    elif opcao == 2:
        numero = int(input("Digite um número: "))
        print("Você digitou:", numero)
    elif opcao == 3:
        print("Saindo do sistema...")
    else:
        print("Opção inválida!")
