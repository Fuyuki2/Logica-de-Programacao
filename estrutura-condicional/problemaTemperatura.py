opcao = str.upper(input("Voce vai digitar a temperatura em qual escala (C/F)? "))

#if opcao == "C" or opcao == "c": também funciona
if opcao == "C":
  celcius = float(input("Digite a temperatura em CELSIUS: "))
  resultado = (celcius * 1.8) + 32
  print(f"Temperatura equivalente em FAHRENHEIT = {resultado:.2f}")
elif opcao == "F":
  fahrenheit = float(input("Digite a temperatura em FAHRENHEIT: "))
  resultado = (fahrenheit - 32) / 1.8
  print(f"Temperatura equivalente em CELCIUS = {resultado:.2f}")
