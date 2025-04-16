import sys

quantidade = int(input("Quantas pessoas serao digitadas? "))

listaAltura = []
alturaF = []
somaAltura = 0
qtdHomens = 0

for i in range(quantidade):  # loop para inserir os dados
    while True:  # loop para verificar o genero correto
        print("Digite 0 para sair")
        genero = input(f"Digite o genero (M/F) da {i+1}ª pessoa: ").upper()

        # verificar o genero
        if genero == "M":
            altura = float(input(f"Digite a altura da {i+1}ª pessoa: "))
            listaAltura.append(altura)
            qtdHomens += 1
            break  # sai do while, avança o for

        elif genero == "F":
            altura = float(input(f"Digite a altura da {i+1}ª pessoa: "))
            listaAltura.append(altura)
            alturaF.append(altura)
            somaAltura += altura
            break  # sai do while, avança o for

        elif genero == "0":
            sys.exit()  # Programa termina aqui

        else:
            print("Genero incorreto! Tente novamente")

menorAltura = min(listaAltura)
maiorAltura = max(listaAltura)

print(f"Menor Altura: {menorAltura}")
print(f"Maior Altura: {maiorAltura}")
if len(alturaF) > 0:
    media = somaAltura / len(alturaF)
    print(f"Media das alturas das mulheres = {media:.2f}")
else:
    print("Nenhuma mulher foi registrada.")
print(f"Numero de homens = {qtdHomens}")
