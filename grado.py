#Temperatura Minima e Maxima

def minMax(temperaturas):
	print("A menor temperatura do mês foi: ", minima(temperaturas), "C.")
	print("A maior temperatura do mês foi: ", maxima(temperaturas), "C.")


def maxima(temps):
	max = temps[0]
	i = 1
	while i < len(temps):
		if temps[i] > max:
			max = temps[i]
		i = i + 1
	return max


def minima(temps):
	min = temps[0]
	i = 1
	while i < len(temps):
		if temps[i] < min:
			min = temps[i]
		i = i + 1
	return min


def testes(temp, valor_esperado):
	valor_calculado = minima(temp)
	if valor_calculado != valor_esperado:
		print("Valor errado para array", temp)
		print("Valor esperado: ", valor_esperado,". Valor calculado: ", valor_calculado)


def testa_minima():
	print("Iniciando os testes")
	testes([0], 0)
	testes([0, 0, 0, 0, 0, 0], 0)
	testes([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 0)
	testes([-15, -12, -2, -34], -34)
	print("Finalizando os testes")


temperaturas = [26, 25, 27, 27, 28, 27, 22, 25, 24, 26, 25, 26, 30, 31, 27, 27, 27, 28, 29, 31]
minMax(temperaturas)
