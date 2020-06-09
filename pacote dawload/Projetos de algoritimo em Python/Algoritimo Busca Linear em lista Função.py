# Implemente uma função chamada busca_linear(lista, num), que recebe uma lista e um número,
# e verifica se o número está na lista usando uma busca linear. A função retorna True ou False.


# definição da função
def busca_linear(variavelMae, variavel):
    status = False
    if variavel in variavelMae:
        status = True
    else:
        status = False
    return status


def busca2Linear(variavelMae, variavel):
    for i in range(len(variavelMae)):
        if variavelMae[i] == variavel:
            return True
    return False


# uso da função
lista = [12, 23, 33, 15, 21, 19, 100, 17]
numero = int(input('Qual numero desejar pesquisar: '))

print(busca2Linear(lista, numero))
