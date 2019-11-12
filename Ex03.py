#Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule
#o total em segundos.

n1 = int(input('Coloque a quantidade de dias: '))
n2 = int(input('Coloque a quantidade de horas: '))
n3 = int(input('Coloque a quantidade de minutos: '))
n4 = int(input('Coloque a quantidade de segundos: '))

print ('Os seus segundos são :', n1*86400 +n2*3600 +n3*60 +n4*1)