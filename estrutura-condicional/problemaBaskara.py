coeficienteA = float(input("Digite o coeficiente A: "))
coeficienteB = float(input("Digite o coeficiente B: "))
coeficienteC = float(input("Digite o coeficiente C: "))

delta = (coeficienteB ** 2) - (4 * coeficienteA * coeficienteC)

if coeficienteA == 0 or delta < 0:
  print("Esta equacao nao possui raizes reais")

elif delta == 0:
  X = (-coeficienteB / (2 * coeficienteA))
  print(f"{X:.4f}")

elif delta > 0:
  X1 = (-coeficienteB + (delta ** 0.5)) / (2 * coeficienteA)
  X2 = (-coeficienteB - (delta ** 0.5)) / (2 * coeficienteA)
  print(f"{X1:.4f}\n{X2:.4f}")
