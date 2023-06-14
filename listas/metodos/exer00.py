frutas = ["maça", "pera", "uva", "amora", "laranja", "mamao"]

print(frutas)

for fruta in frutas:
    print(fruta)

print("tem mamao?")

print("qts mamao: ", frutas.count("mamao")) #metodo count conta quantos itens de um item especificado tem na lista
print("localizacao mamao: ", frutas.index("mamao")) # metodo index, mostra em qual indice esta esse item

print("Adicionando abacaxi: ", frutas.append("abacaxi")) #append adiciona no final da lista

pos = frutas.index("uva")
print(pos)
frutas.insert(pos, "saladas mistas") #metodo insert, insere o item especificado na posicao especificada, e coloca todos os item seguintes uma posicao pra frente na lista
print(frutas)
frutas[pos] = "salada mista" #adiciona salada mista no indice pos, o mesmo que frutas[2] = "salada mista"

print(frutas)

frutas.reverse() #reverte a ordem da lista, do ultimo pro primeiro
print(frutas)

frutas.sort() #organiza em ordem alfabetica ou numerica crescente os itens da lista
print(frutas)