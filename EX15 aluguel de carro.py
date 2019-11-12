dias=int(input('Quantos dia o carro foi alugado?: '))
km = float(input('Qual a kilometragem rodada?: '))
cdias = 60
ckm= 0.15
pago=(dias*cdias) + (km*ckm)
#print('Você utilizou o carro por {:.2f} dia(s) e percorreu {:.2f} km(s), o valor do seu alugue é de R${:.2f}'.format(dias , km , ((dias*cdias)+(km*ckm))))
print('O total a pagar é de R${:.2f}'.format(pago))
