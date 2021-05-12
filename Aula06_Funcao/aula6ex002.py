# 2.	 Faça um programa, com uma função que necessite de um argumento. 
# A função retorna o valor de caractere ‘P’, se seu argumento for positivo,
#  ‘N’, se seu argumento for negativo e ‘0’ se for 0.

def funcao():
    ex2 = int(input('Digitr um número para verificar se é positivo ou negativo: '))
    if ex2 > 0:
        print('P')
    elif ex2 == 0:
        print('0')
    else:
        print('N')
funcao()
