quantidade = int(input("Quantas pessoas voce vai digitar? "))

listaNomes = []
listaIdades = []

# loop para inserir os elementos na lista nomes e idades
for i in range(quantidade):
  print(f"Dados da {i+1}ª pessoa")
  nome = input("Nome: ")
  idade = int(input("Idade: "))
  listaNomes.append(nome)
  listaIdades.append(idade)

# variavel para maior idade
maisVelho = 0

for i in range(1, quantidade): # Começa do segundo elemento
  if listaIdades[i] > listaIdades[maisVelho]:
    maisVelho = i # Atualiza índice do mais velho

# Exibe o nome da pessoa mais velha
print(f"A pessoa mais velha é {listaNomes[maisVelho]} com {listaIdades[maisVelho]} anos.")