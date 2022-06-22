from time import pthread_getcpuclockid


preco = 0
precocusto = 0

for i in range(0,40):
    p = int(input('Preço do produto: '))
    pc = int(input('Preço de custo do produto: '))

    preco = preco + p
    precocusto = precocusto + pc

    if preco > precocusto:
        print('Lucro.')
    else:
        print('Não obteve lucro.')

print('A média dos preços é: %d' %((preco+precocusto)/2))