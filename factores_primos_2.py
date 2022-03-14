def primo (fator):
    num = fator
    if num == 2:
        print("é primo")
    elif num%2==1:
        print("é primo")
    else:
        print("não é primo")


n = int(input("Digite um numero inteiro: "))
fator = 2
multiplicidade = 0

while n > 1:
    while n % fator == 0:
        multiplicidade = multiplicidade + 1
        n = n / fator
    if multiplicidade > 0:
        print ("fator: ",fator, "multiplicidade = ", multiplicidade)
        primo (fator)
    fator = fator + 1
    multiplicidade = 0
