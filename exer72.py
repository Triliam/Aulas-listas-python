lista = ['A', 'B', "C", 'D', 'E']
index = 0

letra = str(input("Escolha uma letra da lista para ser substituida por X: "))

num = lista.index(letra) #encontra o indice
print(num)
lista.remove(letra) #remove esse valor encontrado no indice
print(lista)
lista.insert(num, 'X') #insere o novo valor no indice
print(lista)

 