import textwrap

def deposito():
    print("Depósito")

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

    while True:
        opcao = menu()

        if opcao == "d":
            deposito()
        
        elif opcao == "s":
            sacar()

        elif opcao == "e":
            extrato()
        
        elif opcao == "q":
            break
        
        else: 
            print("Operação inválida, selecione a operação desejada.")


main()