import textwrap

# / => positional only
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR${valor:.2f}\n"
        print("\n#### Depósito realizado com sucesso! ####")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato

#  * => keyword only
def sacar(*,saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n @@@ Operação falhou! Você não tem SALDO suficiente. @@@")
    elif excedeu_limite:
        print("\n @@@ Operação falhou! Você excedeu o LIMITE. @@@")
    elif excedeu_saques:
        print("\n @@@ Operação falhou! Número total de SAQUES excedido. @@@")
    
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: \t\t R$ {valor:.2f}\n"
        print("\n#### Saque realizado com sucesso! ####")
        numero_saques += 1
        # print(numero_saques)
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato, numero_saques

# / => positional only & * => keyword only
def exibir_extrato(saldo, /,*,extrato):
    print("________________________EXTRATO__________________________")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("_________________________________________________________")


def menu(): 
    menu = """\n
    ======== MENU ======== \n
    [d]\t Depositar
    [s]\t Sacar
    [e]\t Extrato
    [q]\t Sair
    => """
    return input(textwrap.dedent(menu))

def main():
    LIMITE_SAQUES = 3
    # AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    # usuarios = []
    # contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato =  depositar(saldo, valor, extrato)
        
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato, numero_saques = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "q":
            break
        
        else: 
            print("Operação inválida, selecione a operação desejada.")


main()