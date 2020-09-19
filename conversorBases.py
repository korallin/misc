
#função que inverte a lista para apresentar o resultado em ordem correta
def inversor(lista):
    resposta = []
    tam = len(lista) - 1

    while tam >= 0:
        resposta.append(lista[tam])
        tam -= 1

    return resposta


# Conversor de Decimal para Binário:
def DecBin(decimal):
    resultado = []

    while decimal > 1:
        add = decimal % 2
        resultado.append(add)
        decimal = int(decimal/2)

    resultado.append(1)
    saida = inversor(resultado)

    print(saida)

# Conversor de Decimal para Octal:
def DecOct(decimal):
    resultado = []

    while decimal > 7:
        add = decimal % 8
        resultado.append(add)
        decimal = int(decimal/8)

    resultado.append(decimal)
    saida = inversor(resultado)

    print(saida)

def DecHex(decimal):
    resultado = []

    while decimal > 15:
        add = decimal % 16
        resultado.append(add)
        decimal = int(decimal/16)

    resultado.append(decimal)
    saida = inversor(resultado)

    for i in range(len(saida)):
        if saida[i] > 9:
            if saida[i] == 10:
                saida[i] = 'A'
            elif saida[i] == 11:
                saida[i] = 'B'
            elif saida[i] == 12:
                saida[i] = 'C'
            elif saida[i] == 13:
                saida[i] = 'D'
            elif saida[i] == 14:
                saida[i] = 'E'
            elif saida[i] == 15:
                saida[i] = 'F'

    print(saida)

DecHex(int(input()))
