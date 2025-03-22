distancia1 = float(input("Digite a distancia 1: "))
distancia2 = float(input("Digite a distancia 2: "))
distancia3 = float(input("Digite a distancia 3: "))

if distancia1 > distancia2 and distancia1 > distancia3:
  print(f"MAIOR DISTANCIA = {distancia1}")
elif distancia2 > distancia1 and distancia2 > distancia3:
  print(f"MAIOR DISTANCIA = {distancia2}")
else:
  print(f"MAIOR DISTANCIA = {distancia3}")
