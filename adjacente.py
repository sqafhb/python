valor = int(input("Digite:"))
restodevalor = 0
sobradevalor = 1
resto = 0
verdadeiro = False
x = 1

while sobradevalor != 0 or verdadeiro:
	restodevalor = valor % 10
	sobradevalor = valor // 10
	resto = sobradevalor % 10
	valor = sobradevalor
	if sobradevalor > 0:
		if restodevalor == resto:
			verdadeiro = True
	if verdadeiro:
		print("os valores são adjacentes!!") 
		break
if sobradevalor == 0:
	print("valores não são adjacentes.")			
	
		

		
	


