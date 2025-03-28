while True:
    primeiraNota = float(input("Digite a primeira nota: "))
    if 0 <= primeiraNota <= 10:
        segundaNota = float(input("Digite a segunda nota: "))
        if 0 <= segundaNota <= 10:
            media = (primeiraNota + segundaNota) / 2
            print(f"Media: {media}")
        else:
            print("Valor inválido para a segunda nota! Tente novamente.")
            continue
    else:
        print("Valor invalido para a primeira nota! Tente novamente.")
        continue

    # Pergunta se o usuário deseja continuar
    continuar = input("Deseja calcular outra media? (s/n): ").lower()
    if continuar != 's':
        break
