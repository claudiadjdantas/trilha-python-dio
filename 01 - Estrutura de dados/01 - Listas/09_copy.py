lista = [1, "Python", [40, 30, 20]]
l2 = lista.copy()

lista.copy()

print(lista)  # [1, "Python", [40, 30, 20]]
print(f"Id da l2: {id(l2)}. Id da lista: {id(lista)}")