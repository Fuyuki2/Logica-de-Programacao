numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))

if numero1 % numero2 == 0 or numero2 % numero1 == 0:
  print(f"{numero1}\n{numero2}\nsao multiplos")
else:
  print(f"{numero1}\n{numero2}\nnao sao multiplos")
