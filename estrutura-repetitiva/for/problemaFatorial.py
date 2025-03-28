valorN = int(input("Digite o valor de N (igual ou menor que 15): "))
cont = 1  # Inicializando a variável cont com 1, pois fatorial começa de 1

# Loop para garantir que o valor de N seja válido
while valorN > 15:
    print("ESCOLHA UM VALOR IGUAL OU MENOR QUE 15!")
    valorN = int(input("Digite o valor de N: "))

# Loop para calcular o fatorial de N
for i in range(valorN, 0, -1):
    cont *= i  # Multiplica cont pelo valor de i a cada iteração

print(f"O fatorial de {valorN} é: {cont}")
