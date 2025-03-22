horaInicial = int(input("Digite a hora de inicio do jogo: "))
horaFinal = int(input("Digite a hora final do jogo: "))

if horaFinal > horaInicial:
  duracao = horaFinal - horaInicial
  print(f"O JOGO DUROU {duracao} HORA(S)")

elif horaFinal < horaInicial:
  duracao = (24 - horaInicial) + horaFinal
  print(f"O JOGO DUROU {duracao} HORA(S)")

elif horaFinal == horaInicial:
  print("O JOGO DUROU 24 HORAS")
