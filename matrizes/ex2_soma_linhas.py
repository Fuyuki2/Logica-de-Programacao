linhas = int(input("Qual a quantidade de linhas da matriz? "))
colunas = int(input("Qual a quantidade de colunas da matriz? "))

matriz = []

for linhas in range(linhas):
    linha = []
    for coluna in range(colunas):
        valor = int(input(f"Digite os elementos da {linhas+1}a. linha: "))
        linha.append(valor)
    matriz.append(linha)

lista_somas = []

for i in range(linhas):
    contador = i
    soma = sum(matriz[i])
    lista_somas.append(soma)

print(f"Vetor Gerado:")
for valor in lista_somas:
    print(valor)
