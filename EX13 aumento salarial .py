#salario=float(input('Qual o salario: '))
#aumento=salario*15/100
#novo=salario+aumento
#print('O seu novo salario é de R${}'.format(novo))


#EXEMPLO 2 PYTHON ZUMBI

#Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a
#porcentagem do aumento. Exiba o valor do aumento e do novo salário.


s = float(input('Valor do salario: '))
p = float(input('Valor do percentual de aumento: '))
aumento = s * p /100
novo = s + aumento
print('Aumento: R$ %.2f' %aumento)
print('Novo salario: R$ %.2f' %novo)


#Guanabara
#salário= float(input('Qual é o salario do funcionário? R$'))
#novo= salário + (salário * 15/100)
#print('Um funcionario que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salário, novo))
