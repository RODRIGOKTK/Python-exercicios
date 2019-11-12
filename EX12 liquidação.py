preco_original=float(input('Este produto custa: '))
desconto=float(input('Valor do desconto:'))
preco_desconto=desconto/100
preco_novo=preco_desconto*preco_original
print('O valor com desconto será de R${}'.format(preco_original-preco_novo))


'''
Guanabara

preço = float(input('Qual é o preço do produto? R$'))
novo = preço - (preço * 5 /100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f} '.format(preço, novo))
'''