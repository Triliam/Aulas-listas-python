primeiroTermo = 2
qtdTermos = 5
razao = 3

for i in range(1, qtdTermos +1): #jeito mais logico que da pra reusar com outras operaçoes matematicas, tipo PG
    print("a", i, "...", primeiroTermo)
    primeiroTermo = primeiroTermo + razao

# for i in range(2,15,3):
#     print (i)

inicio = 4 
raz = 4
qtd = (6 * raz) + 1 #jeito maluco que saiu da minha cabeça, ignorar é uma opcao

for i in range(inicio, qtd, raz):
    print(i)

