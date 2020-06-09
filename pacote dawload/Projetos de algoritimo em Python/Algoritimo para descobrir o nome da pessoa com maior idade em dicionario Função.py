# 4.
# Assuma um dicionário com a seguinte estrutura:
# idades = {'Joao' : 32, 'Maria' : 21, 'Joana' : 22}

# Implemente uma função chamada maior_idade(dic), que recebe o dicionário apresentado e retorne o nome da pessoa
# com a maior idade registrada no dicionário.


def maior_idade(variavel):
    cont = 0
    maior = 0
    fulano = ' '
    for nome, idade in variavel.items():
        if cont == 0:
            maior = idade
            fulano = nome
        else:
            if idade > maior:
                maior = idade
                fulano = nome
        cont = cont + 1
    return fulano

idades = {'Joao': 32, 'Maria': 21, 'Joana': 22}

print(f'A pessoa com maior idade registrada é {maior_idade(idades)}')