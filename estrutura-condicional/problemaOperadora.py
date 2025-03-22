minutos = int(input("Digite a quantidade de minutos: "))

if minutos > 100:
  excedente = (minutos - 100) * 2
  valor = excedente + 50
  print(f"Valor a pagar = R${valor:.2f}")
else:
  print("Valor a pagar = R$50.00")
  