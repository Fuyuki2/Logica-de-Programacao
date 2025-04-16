quantidade = int(input("Quantos numeros voce vai digitar? "))

numeros = []
abaixoDaMedia = []
total = 0

# loop para adicionar o numeros na lista e somar o total
for i in range(quantidade):
  numero = float(input(f"Digite o {i+1}º numero: "))
  numeros.append(numero)
  total += numero

media = total / len(numeros)
print(f"MEDIA DO VETOR = {media:.5}")
for numero in numeros:
  if numero < media:
    abaixoDaMedia.append(numero)
print(f"ELEMENTOS ABAIXO DA MEDIA\n{abaixoDaMedia}")