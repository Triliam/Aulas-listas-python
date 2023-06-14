primeiroTermo = 5
razao = 2
qtd = 5

for i in range (qtd+1):
    print(primeiroTermo)
    primeiroTermo = primeiroTermo * 2 #usando a mesma logica  do exercicio 64, mas agora numa PG


#multiplicar os valores de uma lista por 2
num = [4, 8, 15, 16, 23, 42]

print(num)

for i in range(len(num)):
    num[i] = num[i] * 2

print(num)