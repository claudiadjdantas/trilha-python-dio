import textwrap

#/ => positional only
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR${valor:.2f}\n"
        print("\n#### Depósito realizado com sucesso! ####")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato

def sacar():
    print("Sacar")

def extrato():
    print("Extrato")



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
            print("Sacar")

        elif opcao == "e":
            print("Extrato")
        
        elif opcao == "q":
            break
        
        else: 
            print("Operação inválida, selecione a operação desejada.")


main()