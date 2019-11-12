altura=float(input('Qual a altura da área: '))
largura=float(input('Qual a largura da área: '))
área=largura*altura
tinta=2 #cada litro pinta 2 m²
print('Nesta área será preciso {:.2f} litros de tinta !'.format(área/tinta))

'''
Guanabara

larg=float(input('Largura da parede: '))
alt=float(input('Altura da parede: '))
area= larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))
'''