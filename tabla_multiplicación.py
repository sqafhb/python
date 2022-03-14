#Tabuada

linha = 1
coluna = 1
while linha <= 10:
    while coluna <= 10:
        print(linha * coluna, end = "\t") # "\t" é o tab
        coluna = coluna + 1
    linha = linha + 1
    print() #pula a linha
    coluna = 1