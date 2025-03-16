largura = float(input("Digite a largura: "))
comprimento = float(input("Digite o comprimento: "))
area = largura * comprimento
valor = float(input("Digite o valor do metro quadrado: "))
preco = area * valor

print
print(f"A area do terreno é de R${area} e o preço do terreno é de R${preco}")
