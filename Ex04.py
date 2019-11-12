#Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a
#porcentagem do aumento. Exiba o valor do aumento e do novo salário.


s = float(input('Valor do salario: '))
p = float(input('Valor do percentual de aumento: '))
aumento = s * p /100
novo = s + aumento
print('Aumento: R$ %.2f' %aumento)
print('Novo salario: R$ %.2f' %novo)

