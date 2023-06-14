#Mp = [(N1 x P1) + (N2 x P2) + (N3 x P3) + ... (Nx x Px)] ÷ (P1 + P2 + P3 + ... Px).

#exer de media ponderada, fiz usando lista só pra treinar lista, mas eh bem mais facil sem usar lista
media = 0
provas = 3
peso1 = 3
peso2 = 3
peso3 = 4
notas = []

for i in range(provas): #vai fazer o loop 3 vezes, de 0 até 2
    nota = float(input("digite a nota da prova: "))
    notas.append(nota) #adiciona as tres notas numa lista

print(notas)
  
prova1 = notas[0] * peso1 # acessa o valor que esta no indice 0 da lista e multiplica por 3 

prova2 = notas[1] * peso2
    
prova3 = notas[2] * peso3

media = (prova1 + prova2 + prova3) / (peso1 + peso2 + peso3)

print(media)

if media < 6:
    print("aluno reprovado, ate o prox sementre")