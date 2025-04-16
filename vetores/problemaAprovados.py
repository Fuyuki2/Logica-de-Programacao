quantidade = int(input("Quantos alunos serao digitados? "))

listaNomes = []
listaNota1 = []
listaNota2 = []
listaAprovados = []

for i in range(quantidade): #loop para inserir os valores
  nome = str(input(f"Digite o nome do {i+1}º aluno: "))
  listaNomes.append(nome)
  nota1 = float(input(f"Digite a {i+1}º nota: "))
  listaNota1.append(nota1)
  nota2 = float(input(f"Digite a {i+1}º nota: "))
  listaNota2.append(nota2)
  media = (nota1 + nota2) / 2
  if media >= 6: #verifica se o aluno teve media >= a 6
    listaAprovados.append(nome) #se sim, inserir na lista de aprovados

print("Alunos aprovados:")
for nome in listaAprovados:
    print(listaAprovados)