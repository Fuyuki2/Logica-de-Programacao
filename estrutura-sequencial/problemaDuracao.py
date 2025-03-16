segundos = int(input("Digite a duracao em segundos: "))

dias = segundos // 86400
diaResto = segundos % 86400
horas = diaResto // 3600
horaResto = diaResto % 3600
minutos =  horaResto // 60
segundos = horaResto % 60

print(f"HORARIO {dias}:{horas}:{minutos}:{segundos}")
