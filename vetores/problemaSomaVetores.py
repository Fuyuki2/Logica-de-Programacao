quantidade = int(input("Quantos numeros vai digitar? "))

vetorA = []
vetorB = []
soma = []

# loop para adicionar no vetor A e vetor B
for i in range(quantidade):
  numero = int(input(f"Lista A - Digite o {i+1}º numero: "))
  vetorA.append(numero)
for i in range(quantidade):
  numero = int(input(f"Lista B - Digite o {i+1}º numero: "))
  vetorB.append(numero)

# soma o valor i de cada vetor e adiciona o resultado no vetor "soma"
for i in range(0, quantidade):
  soma.append(vetorA[i] + vetorB [i])
print(f"VETOR RESULTANTE\n{soma}")
