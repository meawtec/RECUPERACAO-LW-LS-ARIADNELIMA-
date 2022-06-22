nome = input("Nome do aluno: ")
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
media = (n1 + n2 + n3)/3

if media >= 7:
    print('Aprovado')
if media <= 5:
    print('Reprovado')
if media >= 5.1 and media <= 6.9:
    print('Recuperacao')