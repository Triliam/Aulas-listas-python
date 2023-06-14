#descobrir o maior valor e sua posicao numa lista.
#diferenca entre os tipo de for

numeros=[0,1,2,3,4,5,6]

num = int(input("Escolha um numero para ser substitiudo por 7: "))

for i in numeros: #assim só mostra e nao altera, tipo foreach - não tem acesso direto aos índices ou à capacidade de modificar os elementos da lista durante o loop.
    if i == num:
        i = 7
    print(i)

print(numeros)

for i in range(len(numeros)): # assim realmente pega o valor da posicao
    if numeros[i] == num:
        numeros[i] = 7

print(numeros)

for i in numeros: 
    print(i)