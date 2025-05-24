tamanho = int(input("Qual a ordem da matriz? "))

matriz = []

for linha in range(tamanho):
    linha_matriz = []
    for coluna in range(tamanho):
        numeros = int(input(f"Elemento[{linha}][{coluna}]: "))
        linha_matriz.append(numeros)
    matriz.append(linha_matriz)

for i in range(tamanho):
    lista_soma = []
    contador = i + 1
    final = len(linha_matriz) - 1
    while contador != final:
        for i in range(linha_matriz):
            lista_soma.append(linha_matriz)
            contador -= 1

soma = sum(lista_soma)
print(soma)
