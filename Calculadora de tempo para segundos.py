#3 horas 23 minutos 17

h = 60 * 60 
m = 60
s = 1

print('Irei te dizer quantos segundos há em qualquer hora')
hora = input('Digite as horas: ')

if hora.isdigit():
	hora_int = int(hora)
	hora_int = hora_int * h
	minuto = input('Digite os minutos:')

	if minuto.isdigit():
		minuto_int = int(minuto)
		minuto_int = minuto_int * m
		
		segundo = input('Digite os segundos: ')

		if segundo.isdigit():
			segundo_int = int(segundo)
			segundo_int = segundo * s
			
			seg_total = int(hora_int) + int(minuto_int) + int(segundo_int)
	
			print(f'O total de segundos nas horas, minutos e segundos digitados são: {seg_total} segundos')
			
		else:
			print('Isso não é um número')
			
	else:
		print('Isso nao é um número')
		
else:
		print('Isso nao é um número')