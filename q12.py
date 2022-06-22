n1 = int(input('Informe um número: '))
n2 = int(input('Informe outro número: '))

if n1 == n2:
    print('Os números {} e {} são iguais.' .format(n1,n2))
else:
    print('Os números {} e {} são diferentes.' .format(n2,n1))
    if n1>n2:
        print('O número {} é maior que o número {}' ,format(n1,n2))
    else:
        print('O número {} é maior que o número {}' .format(n2,n1))