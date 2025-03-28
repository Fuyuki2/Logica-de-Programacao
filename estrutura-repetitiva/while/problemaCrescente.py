valorX = int(input("Digite o valor de X: "))
valorY = int(input("Digite o valor de Y: "))

while valorX != valorY:
  if valorX < valorY:
    print("CRESCENTE")
  else:
    print("DECRESCENTE")
  
  valorX = int(input("Digite o valor de X: "))
  valorY = int(input("Digite o valor de Y: "))
