lista = [0]

num = 1

print("Digite quantos numeros quiser, quando quiser parar aperte 0")
while num !=0: #enquanto num for diferente de zero faça:
    numeros = int(input("digite um numero: "))
    if numeros == 0: #primeira condicao que vai ser lida: qnd o numero que o usuario digitar for 0,
        num = numeros # num recebe numeros, ou seja num recebe 0 e sai do loop
        break # o break pra encerrar o codigo nessa linha
    lista.append(numeros) #adiciona os numeros que o usuario digitar na lista
    print("Lista atualizada")
    print(lista)

lista.sort() # organiza a lista em ordem crescente
print(lista)