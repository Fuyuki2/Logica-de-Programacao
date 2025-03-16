preco = float(input("Digite o preco do produto: ")) 
unidade = int(input("Digite a quanitdade de produtos: "))
dinheiro = float(input("Digite o valor recebido: "))

total = preco * unidade
troco = dinheiro - total
print(f"O valor do troco e de {troco}")
