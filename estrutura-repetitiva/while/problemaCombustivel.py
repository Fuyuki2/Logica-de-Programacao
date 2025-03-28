contAlcool = 0
contGasolina = 0
contEtanol = 0

while True:
  opcao = input("Informe um codigo (1, 2, 3) ou 4 para parar: ")

  if opcao == "1":
    contAlcool += 1
  
  elif opcao == "2":
    contGasolina += 1
  
  elif opcao == "3":
    contEtanol += 1

  elif opcao == "4":
    break # sai do loop

  else:
    print("CODIGO INVALIDO")

# imprime o resultado apos o loop
print(f"MUITO OBRIGADO!\nAlcool:{contAlcool}\nGasolina:{contGasolina}\nEtanol:{contEtanol}")
