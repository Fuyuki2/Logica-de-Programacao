numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))
numero3 = int(input("Digite o terceiro numero: "))

if numero1 < numero2 and numero1 < numero3:
  print(f"O maior numero e {numero1}")
elif numero2 < numero1 and numero2 < numero3:
  print(f"O menor numero e {numero2}")
else:
  print(f"O menor numero e {numero3}")
  