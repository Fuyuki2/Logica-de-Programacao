quantidade = int(input("Quantos elementos vai ter o vetor? "))

listaPares = []
total = 0

for i in range(quantidade):
  numero = int(input(f"Digite o {i+1}º numero: "))
  if numero % 2 == 0:
    listaPares.append(numero)
    total += numero
    media = total / len(listaPares)

if len(listaPares) == 0:
  print("NENHUM NUMERO PAR")
else:
  print(f"MEDIA DOS PARES = {media}")