numeros = [1, 42, 33, 40, 38, 100]

maior = 0
pos = 0

for i in range(len(numeros)):
    print("Na posicao: ", i, ", esta o valor: ", numeros[i])
    if numeros[i] > maior:
        maior = numeros[i]
        pos = i
print("o maior numero é:" , maior, " e a posicao eh: ", pos)