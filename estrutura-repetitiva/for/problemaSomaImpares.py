valorX = int(input("Digite o valor de X: "))
valorY = int(input("Digite o valor de Y: "))
soma = 0

for i in range(valorX, valorY):
  if (i % 2) != 0:
    soma += i
print(soma)
