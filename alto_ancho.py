largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

linha = altura
var = "#"
while linha != 1:
    if linha == altura:
        print (largura*var)
        linha = linha - 1

    while linha >= 1:
        print (var + (" " * (largura - 2)) + var)
        linha = linha - 1
        
        if linha == 1:
            print(largura*var)
            break    
    break

print()