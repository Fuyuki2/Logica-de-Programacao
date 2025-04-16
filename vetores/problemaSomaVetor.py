quantidade = int(input("Quantos numeros voce vai digitar: "))

total = 0
lista = []

for i in range(quantidade): #loop para adicionar os numeros na lista
  numeros = int(input(f"Digite o {i+1}º numero: "))
  lista.append(numeros)
  total += numeros #adiciona e soma os numeros na variavel total
media = total / quantidade

print(lista)
print(total)
print(media)
