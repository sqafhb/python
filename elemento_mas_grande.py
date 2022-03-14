

def maior_elemento(lista):
	maior = list(set(lista))
	menor = (maior[-1])

	if menor <= 0:
		menor = (sorted(lista))
		return (menor[-1])

	else:
		return (maior[-1])


lista = [-90, -27, -12, -50]
num = 0
for numetos in lista:
	num = maior_elemento(lista)
	print (num)
	break
