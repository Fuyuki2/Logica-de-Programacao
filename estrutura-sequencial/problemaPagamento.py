nome = str(input("Digite seu nome: "))
valorHora = int(input("Digite o valor da hora trabalhada: "))
horaTrabalhada = int(input("Digite a quantidade de horas trabalhadas: "))

pagamento = valorHora * horaTrabalhada
print(f"O pagamento para {nome} deve ser R${pagamento}")
