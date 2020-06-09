# 1.
# Assuma uma lista com a seguinte estrutura:
# lista = [12, 23, 33, 15, 21, 19, 100, 17]

# Implemente uma função chamada ordena_invertido(lista), que recebe uma lista, aplica o algoritmo
# insertion sort e devolve a lista ordenada.


def ordena_invertido(variavel):
    segundoElemento = 1
    while segundoElemento < len(variavel):
        atual = variavel[segundoElemento]
        antecessor = segundoElemento - 1
        trocou = False
        while antecessor >= 0 and variavel[antecessor] > atual:
            variavel[antecessor + 1] = variavel[antecessor]
            trocou = True
            antecessor = antecessor - 1
        if trocou:
            variavel[antecessor + 1] = atual
        segundoElemento = segundoElemento + 1
    variavel.reverse()
    return variavel


lista = [12, 23, 33, 15, 21, 19, 100, 17]

print(f'A lista ordenada é {ordena_invertido(lista)}')