minutos=float(input('Minutos utilizados :'))
if minutos < 200:
    tarifação = 0.20
else:
    if minutos <= 400:
        tarifação = 0.18
    else:
        tarifação = 0.15
print ('Conta telefônica: R$%6.2f' %(minutos *tarifação))