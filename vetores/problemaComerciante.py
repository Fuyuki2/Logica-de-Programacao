quantidade = int(input("Serao digitados dados de quantos produtos? "))

lucro_baixo = []
lucro_medio = []
lucro_alto = []
total_compra = 0
total_venda = 0

for i in range(quantidade):  # loop para inserir os dados
    print(f"Produto {i+1}")
    nome = input("Nome: ")
    preco_compra = float(input("Preco de compra: "))
    total_compra += preco_compra
    preco_venda = float(input("Preco de venda: "))
    total_venda += preco_venda
    lucro = ((preco_venda - preco_compra) / preco_compra) * 100
    if lucro < 10:  # verifica o lucro
        lucro_baixo.append(nome)
    elif lucro >= 10 and lucro <= 20:
        lucro_medio.append(nome)
    elif lucro > 20:
        lucro_alto.append(nome)

lucro_total = total_venda - total_compra

print("\nRELATORIO:")
print(f"Lucro abaixo de 10%: {len(lucro_baixo)}")
print(f"Lucro entre 10% e 20%: {len(lucro_medio)}")
print(f"Lucro acima de 20%: {len(lucro_alto)}")
print(f"Valor total de compra: {total_compra:.2f}")
print(f"Valor total de venda: {total_venda:.2f}")
print(f"Lucro total: {lucro_total:.2f}")
