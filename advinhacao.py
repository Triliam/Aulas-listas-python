import random #importa a biblioteca random

segredo = random.randrange(1, 13) #usa a biblioteca random e metodo randrange pra definir um range de numeros aleatorios, no caso vai de 1 ate 13

print(segredo)

print("Jogo da adivinhação! Você possui 3 tentativas!")

#tirando tentativas se numero invalido, e i como contador do loop
for i in range(3): #o loop se repete 3 vezes, de 0 ate 2
    print("Tentativa: ", i+1) # somei 1 ao i para nao aparecer 0, no primeiro loop vai mostrar 1 ao inves de 0
    guess = int(input("Advinhe o numero de 1 até 13: "))
    
    if guess <=0 or guess > 13: #validacao dizendo que se o numero for menor ou igual a zero eh invalido e se o numero for maior que 13 tbm eh invalido
        print("Numero invalido")
        continue #o continue, se true, faz voltar pro inicio do loop, se false continua lendo o codigo pra baixo, no for ele vai continuar contanto pq ta no i o contador

    if i == 2: #2 é o final do loop, coloquei essa condicao aqui pra mostrar a msg que acabou o jogo
        print("Errou. Fim de jogo")
        break # para encerrar o loop e nao seguir lendo as linhas de baixo

    if guess == segredo:
        print("Parabéns, vc adivinhou! O número: ", guess)
        break
    else:
        print("Essa foi a tentativa: ", i+1,". Você errou, tente novamente: ") # se tirar o break ou o continue essa linha ficava sendo exibida
print("o num eh: ", segredo)
   

 #sem tirar tentativa qnd numero invalido e contador no while
tentativas = 3
while(tentativas != 0):
    print("Iniciando tentativas, total de : ", tentativas, " tentativas")
    adv = int(input("Adivinhe o num de 1 até 13: "))

    if adv <= 0 or adv > 13:
        print("num invalido")
        #se tivesse colocado tentativas -=1 aqui, dai sim tiraria uma tentativa das 3, pq while verifica antes de tirar, for segue o loop sem verificar
        continue

    if tentativas == 1:
            print("Fim de jogo")
            break
        
    if adv == segredo:
        print("Acertou miseravi")
        break
    else:
        print("Essa foi a tentativa: ", tentativas,". Você errou, tente novamente: ")
        tentativas -=1
print("o num eh: ", segredo)
