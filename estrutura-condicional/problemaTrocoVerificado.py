preco = float(input("Digite o valor do produto: "))
unidade = int(input("Digite a quantidade deoproduto: "))
dinheiro = float(input("Digite o valor do pagamento: "))

total = preco * unidade
troco = total - dinheiro
if dinheiro < total:
  print(f"Valor insuficiente! Faltam R${troco}")
else:
  print(f"valor do troco = R${troco}")
