quantidade = int(input("Quantos numeros voce vai digitar: "))

for i in range(quantidade):
  numero = int(input("Digite um numero: "))
  
  if numero == 0:
    print("NULO")
  elif numero % 2 == 0:  # Número par
    if numero > 0:
      print("PAR E POSITIVO")
    else:
      print("PAR E NEGATIVO")
  else:  # Número impar
    if numero > 0:
      print("IMPAR E POSITIVO")
    else:
      print("IMPAR E NEGATIVO")
