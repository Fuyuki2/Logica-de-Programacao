ladoA = float(input("Digite o valor do lado A: "))
ladoB = float(input("Digite o valor do lado B: "))
ladoC = float(input("Digite o valor do lado C: "))

if (ladoA + ladoB > ladoC) and (ladoA + ladoC > ladoB) and (ladoB + ladoC > ladoA):

  if ladoA == ladoB == ladoC:
    print("Triangulo equilatero")

  elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
    print("Triangulo isosceles")

  else:
    print("Triangulo escaleno")

else:
  print("Nao e um triangulo")
