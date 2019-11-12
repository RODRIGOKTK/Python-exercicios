#Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média
#esperada para a viagem.

c = input('Qual o seu carro ?')
d = float(input('Qual a distancia para o destino KM ?'))
v = float(input('Qual a velocidade media para a viagem KM/h?'))
t = d / v
print ('O seu/sua',c,'ira demorar aproximadamente %.1f horas para terminar a viagem !' %t)