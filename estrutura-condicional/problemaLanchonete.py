codigoProduto1 = int(5)
codigoProduto2 = float(3.50)
codigoProduto3 = float(4.80)
codigoProduto4 = float(8.90)
codigoProduto5 = float(7.32)

codigoInserido = int(input("Digite o codigo do produto: "))
quantidade = int(input("Digite a quantidade comprada: "))
if codigoInserido == 1:
  valor = codigoProduto1 * quantidade
  print(f"Valor a pagar: R${valor:.2f}")
elif codigoInserido == 2:
  valor = codigoProduto2 * quantidade
  print(f"Valor a pagar: R${valor:.2f}")
elif codigoInserido == 3:
  valor = codigoProduto3 * quantidade
  print(f"Valor a pagar: R${valor:.2f}")
elif codigoInserido == 4:
  valor = codigoProduto4 * quantidade
  print(f"Valor a pagar: R${valor:.2f}")
elif codigoInserido == 5:
  valor = codigoProduto5 * quantidade
  print(f"Valor a pagar: R${valor:.2f}")
else:
  print("Codigo invalido!")
