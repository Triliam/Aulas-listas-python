media = float(input("Digite a media: "))
frequencia = int(input("Digite a frequencia: "))

if frequencia < 75:
    print("Voce foi reprovado")
elif frequencia > 75 and media < 7:
    print("recuperacao")
else:
    print("aprovado")