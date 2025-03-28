valorX = int(input("Digite o valor de X: "))

while valorX != 0:
  # Se X for ímpar, ajusta para o próximo número par
  if valorX  % 2 != 0:
    valorX += 1
   
  # Calcula a soma dos 5 números pares consecutivos
  soma = 5 * valorX + 20

  # Imprime o resultado e solicita o próximo valor de X
  print(f"Soma = {soma}")
  valorX = int(input("Digite o valor de X: "))