'''

    FAZENDO UMA REGRA DE TRÊS CHEGAMOS QUE 144 CIGARROS TIRAM 1 DIA
    DE VIDA DA PESSOA (1 DIA = 1440 MINUTOS = 144 CIGARROS)
'''
cigarros = int(input('Cigarros por dia: '))
anos = int(input('Anos fumados: '))
total_cigarros = anos * 365 * cigarros
dias_perdidos = total_cigarros / 144
anos_perdidos_total= dias_perdidos / 365
meses_perdidos_total= dias_perdidos/12
horas_perdidas_total= dias_perdidos*24
print ('Você perdeu aproximadamente: %.2f anos de sua vida !' %anos_perdidos_total)
print('Você perdeu aproximadamente: %.2f meses de sua vida !'  %meses_perdidos_total)
print('Você perdeu aproximadamente: %.2f dias de sua vida !'  %dias_perdidos)
print('Você perdeu aproximadamente: %.2f horas de sua vida !'  %horas_perdidas_total)
