quantidadeCasos = int(input("Quantos casos voce vai digitar? "))

for i in range(quantidadeCasos):
  numerador = int(input("Entre com o numerador: "))
  denominador = int(input("Entre com o denominador: "))
  if denominador == 0:
    print("DIVISAO IMPOSSIVEL")
  else:
    resultado = numerador / denominador
    print(f"DIVISAO: {resultado}")
quantidade = int(input("Quantos casos voce vai digitar? "))
