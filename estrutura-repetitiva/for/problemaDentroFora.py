quantidade = int(input("Quantos numeros voce vai digitar: "))
dentro = 0
fora = 0

for i in range(quantidade):
  numero = int(input("Digite um numero: "))
  if 10 <= numero <= 20:
    dentro += 1
  else:
    fora += 1
print(f"Dentro:{dentro}\nFora:{fora}")
