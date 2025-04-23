numeroN = int(input("Qual a ordem da matriz? "))

matriz = []

# Leitura da matriz
for i in range(numeroN):
    linha = []
    for j in range(numeroN):
        valor = int(input(f"Digite o valor da posição [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

# Mostrar diagonal principal

print("Diagonal principal:")
for i in range(numeroN):
    print(matriz[i][i], end=" ")
print

# Contar valores negativos
negativo = 0
for i in range(numeroN):
    for j in range(numeroN):
        if matriz[i][j] < 0:
            negativo += 1
print(f"Quantidade de negativos: {negativo}")
