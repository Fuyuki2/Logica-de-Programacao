salarioAtual = float(input("Digite o salario atual: "))

if salarioAtual <= 1000:
  salarioNovo = salarioAtual + (salarioAtual * 20 / 100)
  aumento = salarioAtual * 20 / 100
  print(f"Novo salario = R${salarioNovo}\nAumento = R${aumento}\nPorcentagem = 20%")

elif salarioAtual > 1000 and salarioAtual <= 3000:
  salarioNovo = salarioAtual + (salarioAtual * 15 / 100)
  aumento = salarioAtual * 15 / 10
  print(f"Novo salario = R${salarioNovo}\nAumento = R${aumento}\nPorcentagem = 15%")

elif salarioAtual > 3000 and salarioAtual <= 8000:
  salarioNovo = salarioAtual + (salarioAtual * 10 / 100)
  aumento = salarioAtual * 10 / 100
  print(f"Novo salario = R${salarioNovo}\nAumento = R${aumento}\nPorcentagem = 20%")

elif salarioAtual > 8000:
  salarioNovo = salarioAtual + (salarioAtual * 5 / 100)
  aumento = salarioAtual * 5 / 100
  print(f"Novo salario = R${salarioNovo}\nAumento = R${aumento}\nPorcentagem = 20%")
