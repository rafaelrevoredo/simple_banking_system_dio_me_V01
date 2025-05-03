import textwrap

#PAREI NO 10:11 [VIDEO]

def menu():
    menu = """\n
    ================== MENU ==================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar Contas
    [nu]\tNovo usuário
    [q]\tSair
    =>"""
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n ==== Depósito realizado com sucesso ====")

    else:
        print("\n @@@@ A Operação falhou! O valor é inválido. @@@@")
    
    return(saldo, extrato)

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@@ A operação falhou! Não tem saldo suficiente para realizar esta operação")

    elif excedeu_limite:
        print("\n@@@@ A operação falhou! O valor excede o limite diário")

    elif excedeu_saques:
        print("\n@@@@ A operação falhou! O número máximo de saques foi excedido")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n==== Saque realizado com sucesso ====")

    else:
        print("\n@@@@ A operação falhou! O valor informado é inválido @@@@")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n============== Extrato ==============")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o seu CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@@ Já existe um usuário com este CPF! @@@@")
        return

    nome = input("Por favor, digite seu nome completo: ")
    data_nascimento = input("Por favor, digite a data de nascimento (formato: dd-mm-aaaa): ")
    endereco = input("Por favor insira o seu endereço (Logradouro - número - bairro - cidade/Estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("===== Usuário criado com sucesso, o sr(a) já pode usar o banco. =====")
    
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite o CPF do usuário: ")
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        print("\n==== Conta criada com SUCESSO!====")
        return{"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n@@@@ Usuário não encontrado, fluxo de criação de contas encerrado! @@@@")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                    saldo=saldo,
                    valor=valor,
                    extrato=extrato,
                    limite=limite,
                    numero_saques=numero_saques,
                    limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

main()