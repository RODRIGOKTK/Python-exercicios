#resolução #1

import math
num = float(input('Qual um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, math.trunc(num)))

#resolução #2

import math import trunc
num = float(input('Qual um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))

#resolução #3 sem importação

num = float(input('Qual um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))