from random import randint

# pedir tamanho da matriz (1 a 10)
tamanho_linha = int(input("Qual o tamanho da linha (1 a 10)? "))
while tamanho_linha < 1 or tamanho_linha > 10:
    tamanho_linha = int(input("Digite um numero valido para linha (1 a 10): "))

tamanho_coluna = int(input("Qual o tamanho da coluna (1 a 10)? "))
while tamanho_coluna < 1 or tamanho_coluna > 10:
    tamanho_coluna = int(input("Digite um numero valido para coluna (1 a 10): "))

matriz = []

# gerar matriz quadrada aleatoria
for linha in range(tamanho_linha):
    linha = []
    for coluna in range(tamanho_coluna):
        elementos = randint(1, 10)
        linha.append(elementos)
    matriz.append(linha)

# contar frequencia de cada valor
contagem = {}

for linha in matriz:
    for valor in linha:
        if valor in contagem:
            contagem[valor] += 1
        else:
            contagem[valor] = 1

# separar valores repetidos e nao repetidos
repetidos = []
nao_repetidos = []

for linha in matriz:
    for valor in linha:
        if contagem[valor] > 1:
            repetidos.append(valor)
        else:
            nao_repetidos.append(valor)

# somar os valores
soma_repetidos = sum(repetidos)
soma_nao_repetidos = sum(nao_repetidos)

# imprimir matriz
print("Matriz gerada:")
for linha in matriz:
    for valor in linha:
        print(f"{valor:3}", end=" ")
    print()
print()
print(f"Soma dos valores repetidos: {soma_repetidos}")
print(f"Soma dos valores não repetidos: {soma_nao_repetidos}")
