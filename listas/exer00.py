lista = ["Amanda", "Roberta", "Camila", "Nair", "Nadia"]

lista3 = lista #uma lista recebe os mesmos valores de outra lista, fora do loop
print(lista3) #imprimi os valores da lista 

print(lista[0]) # imprime o valor que esta no indice 0 (primeira posicao) da lista

# for i in range (0,5,2):
#     print(i)
#     print(lista[i])

lista0=[]

for i in range (0,len(lista),2): #inicia no 0, vai até o tamanho da lista (len), pulando de 2 em 2
    print(i)
    print(lista[i])
    lista0.append(lista[i]) #forma de adicionar valores de uma lista em outra, nesse caso adiciona na lista0 o valor que esta no indice 0, 2, 4, pq pula de dois em dois

print("-----------------")
print(lista0)
print("-----------------")

lista2=[]

for i in lista: #esse tipo de for nao acessa valores nos indices (nao da pra modificar valores usando esse for), ele apenas imprimi os valores, tipo um print
    print(i)
    lista2.append(i) #mas é possivel adicionar valores de uma lista em outra lista com o metodo append
    
print("-----------------")

print(lista2)

numeros = [1, 22, 3, 42, 5]

for i in range(len(numeros)): # com esse for (range) é possivel acessar e modificar valores da lista
    print ("i vale:" ,i)
    print(numeros[i])

for i in range(len(numeros)):
    print ("i vale:" ,i)
    print(numeros[i]+3)

print("-----------------")
for i in numeros:
    print ("i vale:" ,i)
    print (i+4)
print("-----------------")

