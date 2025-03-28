quantidadeCasos = int(input("Quantos casos de teste serao digitados? "))
macacos = 0
coelhos = 0
ratos = 0

for i in range(quantidadeCasos):
  quantidadeCobaias = int(input("Digite a quantidade de cobaias: "))
  print("Macaco: M\nRato: R\nCoelho: C")
  tipoCobaia = input("Digite o tipo de cobaia: ").upper()  # garantir que seja maiúsculo

  # garantir que o valor inserido esteja correto
  if tipoCobaia == "M" or tipoCobaia == "R" or tipoCobaia == "C": 
    if tipoCobaia == "M":
      macacos += quantidadeCobaias
    elif tipoCobaia == "R":
      ratos += quantidadeCobaias
    elif tipoCobaia == "C":
      coelhos += quantidadeCobaias
  else:
    print("Tipo inválido! Tente novamente.")

# Calcular o total e os percentuais
total = macacos + coelhos + ratos
percentualM = (macacos / total) * 100
percentualR = (ratos / total) * 100
percentualC = (coelhos / total) * 100

# Exibir resultados
print(f"""
Total de cobaias: {total}
Total de macacos: {macacos}
Total de ratos: {ratos}
Total de coelhos: {coelhos} 
Percentual de macacos: {percentualM:.2f}%
Percentual de ratos: {percentualR:.2f}%
Percentual de coelhos: {percentualC:.2f}%
""")
