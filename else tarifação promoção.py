minutos=float(input('Minutos utilizados :'))
if minutos < 200:
    tarifação = 0.20
else:
    if minutos <= 400:
        tarifação = 0.18
    else:
        if minutos <= 800:
            tarifação = 0.15
        else:
            tarifação = 0.08

print('Conta telefônica: R$%6.2f' % (minutos*tarifação))