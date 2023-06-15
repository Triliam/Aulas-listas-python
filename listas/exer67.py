valorDoProduto = float(input("Digite o valor do produto: "))
valorDoJuros = valorDoProduto * 0.07
valorTotal = valorDoProduto + valorDoJuros
parcelas = valorTotal / 10

print("O valor total é: ", valorTotal, ". O valor das parcelas e´: ", parcelas)