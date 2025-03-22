glicose = float(input("Digite a quantidade de glicose: "))

if glicose <= 100:
  print("Classificacao: NORMAL")
elif glicose > 100 and glicose <= 140:
  print("Classificacao: ELEVADO")
elif glicose > 140:
  print("Classificacao: DIABETES")
