from random import shuffle
n1 = str(input('O primeiro aluno: '))
n2 = str(input('O segundo aluno: '))
n3 = str(input('O terciro aluno: '))
n4 = str(input('O quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será {} !'.format(lista))