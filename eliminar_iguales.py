def remove_iguais(lista):
	remove = list(set(lista))
	return remove


lista = [7, 3, 33, 12, 3, 3, 3, 12, 3, 3, 3, 7, 12, 100]
for n in lista:
	remove = remove_iguais(lista)
	print (sorted(remove))
	break


