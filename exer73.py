numeros = [4, 8, 15, 16, 23, 42]
numMult = []

for i in numeros:
    print(i)

for i in numeros: #usando esse tipo de for, da pra criar uma outra lista com os valores da primeira lista multiplicados por 2
    multiplica = i * 2 #multiplica cada valor por 2 e 
    print(multiplica)
    numMult.append(multiplica) #vai adicionando cada valor nessa lista

print(numMult)

for i in range(len(numeros)): #usando esse for, da pra acessar o valor da lista e modificar a propria lista
    numeros[i] = numeros[i] * 2

print(numeros)