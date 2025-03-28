valorX = int(input("Digite o valor de X: "))
valorY = int(input("Digite o valor de Y: "))

while valorX != 0 and valorY != 0:

  if valorX > 0 and valorY > 0:
    print("Q1")
  
  elif valorX < 0 and valorY > 0:
    print("Q2")
  
  elif valorX > 0 and valorY < 0:
    print("Q4")
  
  elif valorX < 0 and valorY < 0:
    print("Q3")

  valorX = int(input("Digite o valor de X: "))
  valorY = int(input("Digite o valor de Y: "))
