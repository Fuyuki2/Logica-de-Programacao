while True:
  quantidade = int(input("Quantos numeros voce vai digitar (maximo 10): "))

  #verifica se o valor esta correto
  if quantidade < 1 or quantidade > 10:
    print("Valor invalido! Digite um numero de 1 a 10")
    continue
  else:
    lista = []
    for i in range(quantidade): #loop para adicionar os numeros na lista
      numero = int(input(f"Digite o {i+1}º numero: "))
      lista.append(numero)
    
    #verifica se o numero na lista é negativo
    for numero in lista:
      if numero < 0:
        print(numero)
        