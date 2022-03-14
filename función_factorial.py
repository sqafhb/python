def fatorial (n):
    fatorial = 1
    while n > 0:
        fatorial = fatorial * n
        n = n - 1
    return fatorial


n = int(input("Digite um numero inteiro: "))
while n > 0:
    print(fatorial(n))
    break

