ch = 0
cm = 0
for i in range(0,5):
    nome = input('Escreva seu nome: ')
    sexo = str(input('Escreva seu sexo: '))

if sexo == 'masculino':
    ch = ch +1
    print('Você é homem')
elif sexo == 'feminino':
    cm = cm +1
    print('Você é mulher')

print('O número de mulheres é: {}'.format(cm))
print('O número de homens é: %d' %ch)