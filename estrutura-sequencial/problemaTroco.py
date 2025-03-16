preco = float(input("Digite o preco do produto: ")) 
unidade = int(input("Digite a quanitdade de produtos: "))
dinheiro = float(input("Digite o valor recebido: "))

troco = dinheiro - (preco * unidade)
print(f"O valor do troco e de {troco}")
