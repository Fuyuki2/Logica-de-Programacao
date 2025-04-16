quantidade = int(input("Quantos numeros voce vai digitar: "))

numeroPar = []

for i in range(quantidade): 
  numero = int(input(f"Digite o {i+1}º: "))
  if numero % 2 == 0: # verifica se é par
    numeroPar.append(numero)

print(f"Numeros pares:\n{numeroPar}")
print(f"Quantidade de pares: {len(numeroPar)} ")
