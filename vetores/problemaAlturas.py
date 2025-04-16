quantidade = int(input("Quantas pessoas serao digitadas: "))

listaNome = []
listaIdade = []
listaAltura = []
nomeFiltro = []
totalAltura = 0
idadeFiltro = 0  # Contador para pessoas com menos de 16 anos

for i in range(quantidade):
  print(f"Digite os dados da {i+1}ª pessoa")

  nome = input("Nome: ")
  idade = int(input("Idade: "))
  altura = float(input("Altura: "))

  listaNome.append(nome)
  listaIdade.append(idade)
  listaAltura.append(altura)
  totalAltura += altura

  if idade < 16:
    nomeFiltro.append(nome)
    idadeFiltro += 1 # Contador de menores de 16 anos

# Cálculo da média de altura
media = totalAltura / quantidade

# Cálculo da porcentagem de pessoas com menos de 16 anos
porcentagem = (idadeFiltro / quantidade) * 100

print(f"\nAltura média: {media:.2f}")
print(f"Pessoas com menos de 16 anos: {porcentagem:.2f}%")

if nomeFiltro:
    print("Nomes:")
    for nome in nomeFiltro:
        print(nome)
else:
    print("Nenhuma pessoa com menos de 16 anos.")
