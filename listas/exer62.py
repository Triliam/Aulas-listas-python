numeros = [1, 42, 33, 0, 40, -90, 38, 100]

#descobrir o maior numero da lista e em qual posicao ele esta
maior = 0
pos = 0

for i in range(len(numeros)):
    print("Na posicao: ", i, ", esta o valor: ", numeros[i])
    if numeros[i] > maior:
        maior = numeros[i]
        pos = i
print("o maior numero é:" , maior, " e a posicao eh: ", pos)

#descobrir o menor numero na lista e em qual posicao ele esta
menor = maior
posMenor = 0

for i in range (len(numeros)):
    if numeros[i] < menor:
        menor = numeros[i]
        posMenor = i

print("O menor eh: ", menor, ". Na posicao: ", posMenor)
