idade = int(input("Digite sua idade: "))
soma = 0
cont = 0

while idade >= 0:
  soma = soma + idade
  cont += 1
  idade = int(input("Digite sua idade: "))

if cont < 0:
  print("IMPOSSIVEL CALCULAR")
else:
  media = soma / cont
  print(f"{media:.2f}")
  