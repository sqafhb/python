#largura x altura

largura = int(input("Digite o valor da largura: "))
altura = int(input("Digite o valor da altura: "))

coluna = 0
linha = 0

while altura != linha:
    while largura != coluna:
        var = "#"
        print(largura*var,)
        coluna = largura
    linha = linha + 1
    coluna = 0