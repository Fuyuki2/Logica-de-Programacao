from random import randint

# pedir tamanho da matriz (1 a 10)
tamanho_linha = int(input("Qual o tamanho da linha (1 a 10)? "))
while tamanho_linha < 1 or tamanho_linha > 10:
    tamanho_linha = int(input("Digite um numero valido para linha (1 a 10): "))

tamanho_coluna = int(input("Qual o tamanho da coluna (1 a 10)? "))
while tamanho_coluna < 1 or tamanho_coluna > 10:
    tamanho_coluna = int(input("Digite um numero valido para coluna (1 a 10): "))

# gerar matriz quadrada aleatoria
matriz = []

for linha in range(tamanho_linha):
    linha = []
    for coluna in range(tamanho_coluna):
        elementos = randint(1, 20)
        linha.append(elementos)
    matriz.append(linha)

# achar quais sao os valores repetidos e a quantidade

valores_repetidos = {}

for linha in matriz:
    for valor in linha:
        valores_repetidos[valor] = valores_repetidos.get(valor, 0) + 1

# separar valores repetidos e nao repetidos
repetidos = []
nao_repetidos = []

for valor in valores_repetidos:
    if valores_repetidos[valor] == 1:
        nao_repetidos.append(valor)
    else:
        repetidos.append(valor)

# somar os valores
soma_repetidos = 0
soma_nao_repetidos = 0

for valor, qtde in valores_repetidos.items():
    if qtde == 1:
        soma_nao_repetidos += valor
    else:
        soma_repetidos += valor * qtde

# imprimir matriz
print("Matriz gerada:")
for linha in matriz:
    for valor in linha:
        print(f"{valor:3}", end=" ")
    print()
print()
print(f"Soma dos valores repetidos: {soma_repetidos}")
print(f"Soma dos valores não repetidos: {soma_nao_repetidos}")
print(f"Quantidade de valores repetidos: {valores_repetidos}")
print(f"Valores repetidos: {repetidos}")
print(f"Valores nao repetidos: {nao_repetidos}")
