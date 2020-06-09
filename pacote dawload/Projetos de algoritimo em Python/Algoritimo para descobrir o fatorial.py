# 3.
# Considere o fatorial de um número n como a multiplicação dos números de 1 a n.
# Assim, para n = 5, o fatorial de 5 é 5 * 4 * 3 * 2 * 1 = 120.
# Implemente uma função chamada fatorial(n) usando For. Ela recebe um valor n retorna o seu fatorial.



def fatorial(n):
    calculo = 1
    for c in range(n, 0, -1):
        calculo = calculo * c
    return calculo


numero = int(input('Digite um número para calcular seu fatorial: '))

print(f'O fatorial do número é {fatorial(numero)}')
