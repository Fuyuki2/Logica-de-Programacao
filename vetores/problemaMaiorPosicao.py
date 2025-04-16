quantidade = int(input("Quantos numeros voce vai digitar: "))

numeros = []

for i in range(quantidade): 
  numero = int(input(f"Digite o {i+1}º: "))
  numeros.append(numero)

if numeros:  # Verifica se a lista não está vazia
  maior = numeros[0]  # Inicializa com o primeiro número
  posicao = 0  # Inicializa a posição do maior número

  for i, num in enumerate(numeros):  # Percorre a lista com índices
    if num > maior:
      maior = num
      posicao = i  # Atualiza a posição do maior número

  print(f"Maior valor: {maior}")
  print(f"Posição: {posicao+1}")  # Índice começa do 0
else:
  print("Nenhum número foi inserido.")
