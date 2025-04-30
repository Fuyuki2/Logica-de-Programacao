ordem = int(input("Qual a ordem da matriz? "))

matriz = []
maiores_valores = []

for linha in range(ordem):
    linha_matriz = []
    for coluna in range(ordem):
        elemento = int(input(f"Elemento: [{linha}][{coluna}]: "))
        linha_matriz.append(elemento)
    matriz.append(linha_matriz)
    maior_valor = max(linha_matriz)
    maiores_valores.append(maior_valor)

print("MAIOR ELEMENTO DE CADA LINHA:")
print(maiores_valores)
