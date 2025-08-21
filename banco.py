def menu():
    print("\n===== MENU =====")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Extrato")
    print("4 - Criar Usuário")
    print("5 - Criar Conta Corrente")
    print("0 - Sair")
    return int(input("Escolha uma opção: "))


def depositar(saldo, extrato):
    valor = float(input("\nDigite o valor para depósito: "))
    if valor <= 0:
        print("❌ Valor inválido para depósito ❌")
    else:
        saldo += valor
        extrato.append(f"Depósito: R${valor:.2f}")
        print(f"✅ Depósito de R${valor:.2f} realizado com sucesso!")
    return saldo, extrato


def sacar(saldo, extrato, limite_saques, saques_realizados):
    if saques_realizados >= limite_saques:
        print("❌ Limite diário de saques atingido ❌")
        return saldo, extrato, saques_realizados

    valor = float(input("\nDigite o valor para saque: "))
    if valor > saldo:
        print("❌ Saldo insuficiente ❌")
    elif valor > 500:
        print("❌ Valor máximo por saque é R$500 ❌")
    elif valor <= 0:
        print("❌ Valor inválido ❌")
    else:
        saldo -= valor
        saques_realizados += 1
        extrato.append(f"Saque: R${valor:.2f}")
        print(f"✅ Saque de R${valor:.2f} realizado com sucesso!")

    return saldo, extrato, saques_realizados


def mostrar_extrato(saldo, extrato):
    print("\n===== EXTRATO =====")
    if extrato:
        for mov in extrato:
            print(mov)
    else:
        print("Nenhuma movimentação realizada.")
    print(f"Saldo atual: R${saldo:.2f}")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario_existente = next((u for u in usuarios if u["cpf"] == cpf), None)

    if usuario_existente:
        print("❌ Já existe usuário com esse CPF ❌")
        return usuarios

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print(f"✅ Usuário {nome} criado com sucesso!")
    return usuarios


def criar_conta_corrente(agencia, usuarios, contas):
    cpf = input("Informe o CPF do usuário: ")
    usuario = next((u for u in usuarios if u["cpf"] == cpf), None)

    if not usuario:
        print("❌ Usuário não encontrado, crie o usuário primeiro ❌")
        return contas

    numero_conta = len(contas) + 1
    contas.append({"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario})
    print(f"✅ Conta corrente {numero_conta} criada com sucesso para {usuario['nome']}!")
    return contas


def main():
    saldo = 0
    extrato = []
    limite_saques = 3
    saques_realizados = 0
    usuarios = []
    contas = []
    AGENCIA = "0001"

    while True:
        opcao = menu()

        if opcao == 1:
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == 2:
            saldo, extrato, saques_realizados = sacar(saldo, extrato, limite_saques, saques_realizados)
        elif opcao == 3:
            mostrar_extrato(saldo, extrato)
        elif opcao == 4:
            usuarios = criar_usuario(usuarios)
        elif opcao == 5:
            contas = criar_conta_corrente(AGENCIA, usuarios, contas)
        elif opcao == 0:
            print("✅ Operação finalizada. Até logo!")
            break
        else:
            print("❌ Opção inválida, tente novamente ❌")


main()
