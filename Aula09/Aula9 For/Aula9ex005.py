n = int(input('Digite um nùmero inteiro: '))
print('os divisores de ', n, 'são')

contador = 0
for i in range(n,0,-1):
    if(n % 1 == 0):
        print(i)
        contador += 1
if contador ==2:
    print(n, 'è um numero primo!')