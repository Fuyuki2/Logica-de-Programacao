linhas = int(input("Qual a quantidade de linhas da matriz? "))
colunas = int(input("Qual a quantidade de colunas da matriz? "))

matriz = []

for linha in range(linhas):
    linha_matriz = []
    for coluna in range(colunas):
        valor = int(input(f"Elemento [{linha}][{coluna}]"))
        matriz.append(valor)
        linha_matriz.append(valor)  # adiciona o valor na linha
    matriz.append(linha_matriz)  # adiciona a linha na matriz

negativo = []

for value in matriz:
    if value < 0:
        negativo.append(value)

print(f"Valores Negativos: {negativo}", end=" ")
