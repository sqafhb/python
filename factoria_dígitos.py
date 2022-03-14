# Fatorial de numeros digitados com repetições encaixadas "2 whiles"

n = int(input("Digite um numero inteiro "))
while n >= 0:
    fatorial = 1
    while n > 0:
        fatorial = fatorial * n
        n = n - 1
    print(fatorial)
    n = int(input("Digite um numero inteiro "))