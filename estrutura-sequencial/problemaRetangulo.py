import math
base = float(input("Digite a base do retangulo: "))
altura = float(input("Digite a altura do retangulo: "))

area = base * altura
perimetro = (2 * base) + (2 * altura)
diagonal = ((base ** 2) + (altura ** 2)) ** 0.5
#tambem posso importar math e usar math.sqrt
#math.sqrt((base ** 2) + (altura ** 2))

print(f"O retangulo possui uma area de {area:.4f}, perimetro de {perimetro:.4f} e diagonal de {diagonal:.4f}")
