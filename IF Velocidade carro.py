velocidade_carro=int(input('A velocidade do carro: '))
velocidade_limite=110
if velocidade_carro > velocidade_limite :
    print('Seu carro foi multado !')
    multa= (velocidade_carro - velocidade_limite)*5
    print ('Valor da multa: R$ %5.2f' %multa)
if velocidade_carro < velocidade_limite:
    print('Carro sem multa !')
if  velocidade_carro == velocidade_limite:
    print('Carro no limite de velocidade permitido !')