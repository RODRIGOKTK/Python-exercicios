n = 1
soma = 0
while n <= 10:
    x = float(input('Digite o %d° numero: ' %n))
    soma = soma + x
    n = n + 1
    print('Previa: %d' %soma)
print ('Media: %d' % (soma/10))