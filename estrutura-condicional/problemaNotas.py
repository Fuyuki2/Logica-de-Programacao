nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))

notaFinal = nota1 + nota2
if notaFinal < 60:
  print(f"REPROVADO. Nota Final = {notaFinal:.1f}")
else:
  print(f"APROVADO. Nota Final = {notaFinal:.1f}")
  