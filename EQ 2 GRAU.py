A=int(input('Valor de A: '))
B=int(input('Valor de B: '))
C=int(input('Valor de C: '))
print('Sua equação é: {}x²{}x{}=0'.format(A, B, C))
D=(B**2)-(4*A*C)
print('Delta vale: {}'.format(D))
RQ=D**(1/2)
X1=((-B)+RQ)/(A*2)
print('O valor de X1 = {}'.format(X1))
X2=((-B)-RQ)/(A*2)
print('O valor de X2 = {}'.format(X2))
S=X1,X2
print('A solução é = {}'.format(S))

