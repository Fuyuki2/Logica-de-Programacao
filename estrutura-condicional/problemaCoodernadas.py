valorX = float(input("Digite o valor de X: "))
valorY = float(input("Digite o valor de Y: "))

if valorX == 0 and valorY == 0:
  print("Origem")

elif valorX == 0:
  print("Eixo Y")

elif valorY == 0:
  print("Eixo X")

elif valorX > 0 and valorY > 0:
  print("Q1")

elif valorX > 0 and valorY < 0:
  print("Q4")

elif valorX < 0 and valorY > 0:
  print("Q2")

elif valorX < 0 and valorY < 0:
  print("Q3")
