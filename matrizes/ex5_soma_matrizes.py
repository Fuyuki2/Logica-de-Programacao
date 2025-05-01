linhas = int(input("Quantas linhas vai ter cada matriz? "))
colunas = int(input("Quantas colunas vai ter cada matriz? "))

matrizA = []
matrizB = []
matrizC = []

print("Digite os valores da matriz A:")
for linha in range(linhas):
    linha_matriz = []
    for coluna in range(colunas):
        numeros = int(input(f"Elemento[{linha}][{coluna}]:"))
        linha_matriz.append(numeros)
    matrizA.append(linha_matriz)

print("Digite os valores da matriz B:")
for linha in range(linhas):
    linha_matriz = []
    for coluna in range(colunas):
        numeros = int(input(f"Elemento[{linha}][{coluna}]:"))
        linha_matriz.append(numeros)
    matrizB.append(linha_matriz)

for linha in range(linhas):
    linha_soma = []
    for coluna in range(colunas):
        soma = matrizA[linha][coluna] + matrizB[linha][coluna]
        linha_soma.append(soma)
    matrizC.append(linha_soma)

print(f"MATRIZ SOMA: {matrizC}")
