#Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o
#preço a pagar

#M = mercadoria
m = float(input('Valor da mercadoria: '))
#P = porcentagem desconto
p = float(input('Porcentagem de desconto: '))
#D = desconto
d = m * p / 100
v = m - d
#V = valor a pagar
print('Desconto: R$ %.2f' %d)
print('Preço a pagar: R$ %.2f' %v)