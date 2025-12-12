
def deposito():
    print("Depósito")

def sacar():
    print("Sacar")

def extrato():
    print("Extrato")


def menu(): 
    
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    => """

    while True:
        opcao = input(menu)

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

def main():
    print("Entrou no main")
    menu()

main()