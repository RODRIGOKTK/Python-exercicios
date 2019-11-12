minutos = int(input('Minutos utilizados: '))
if minutos < 200:
    tarifação = 0.20
elif minutos <= 400:
    tarifação = 0.18
elif minutos <= 800:
    tarifação = 0.15
else:
    tarifação = 0.08
print('Conta telefônica: R$%6.2f' % (minutos*tarifação))