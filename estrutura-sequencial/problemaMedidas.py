valorA = float(input("Digite a medida de A: "))
valorB = float(input("Digite a medida de B: "))
valorC = float(input("Digite a medida de C: "))

areaQuadrado = valorA ** 2
areaTriangulo = (valorA * valorB) / 2
areaTrapezio = ((valorA + valorB) * valorC) / 2

print(f"AREA DO QUADRADO = {areaQuadrado:.4f}")
print(f"AREA DO TRIANGULO = {areaTriangulo:.4f}")
print(f"AREA DO TRAPEZIO = {areaTrapezio:.4f}")
