ordem = int(input("Qual a ordem da matriz? "))

matriz = []

# verifica se o tamanho esta no padrão
if ordem > 10 or ordem < 0:
    ordem = int(input("Numero invalido! Digite novamente: "))

# cria a matriz e aloca os elementos
for linha in range(ordem):
    linhas = []
    for coluna in range(ordem):
        elementos = int(input(f"Elemento[{linha}][{coluna}]"))
        linhas.append(elementos)
    matriz.append(linhas)

soma_positivos = 0

# soma os valores positivos
for linha in matriz:
    for valor in linha:
        if valor > 0:
            soma_positivos += valor

escolha_linha = int(input("Escolha um linha: "))
linha_escolhida = matriz[escolha_linha]
print(f"LINHA ESCOLHIDA:{linha_escolhida}]")

escolha_coluna = int(input("Escolha uma coluna: "))
coluna_escolhida = matriz[escolha_coluna]
print(f"COLUNA ESCOLHIDA:{coluna_escolhida}")

# print da diangona principal
print("Diagonal principal:")
for i in range(matriz):
    print(matriz[i][i], end=" ")
