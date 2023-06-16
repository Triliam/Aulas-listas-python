lista = [0]

num = 1

print("Digite quantos numeros quiser, quando quiser parar aperte 0")
while num !=0: #enquanto num for diferente de zero faça:
    numeros = int(input("digite um numero: "))
    if numeros == 0: #primeira condicao que vai ser lida: qnd o numero que o usuario digitar for 0,
        #num = numeros  #num recebe numeros, ou seja num recebe 0,  eh uma forma de sair do loop, e vai terminar de ler as linhas dentro do escopo do loop, e o 0 entra na lista
        break  #o break pra encerrar o loop nessa linha e n ler as de baixo (que estao no escopo do loop) Assim o 0 nao entra na lista
    lista.append(numeros) #adiciona os numeros que o usuario digitar na lista
    print("Lista atualizada")
    print(lista)

lista.sort() # organiza a lista em ordem crescente
print(lista)
