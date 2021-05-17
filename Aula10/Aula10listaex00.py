# Ex:1 Escreva um programa que pede a senha ao usuário,
# e só sai do looping quando digitarem corretamente a senha.

# senha = 'Fsa0511'
# entrada = input('Digite sua senha')

# while entrada != senha:
#     print('senha incorreta')
#     entrada = input('digite a sua senha novamente: ')
# print('senha correta')

# Exercício 0 – Crie um laço while que vai pedir para o usuário dois números 
# e faça a soma dos dois. Enquanto a soma não for 50, ele deve continuar repetindo.

num1 = int(input('digite um numero: '))
num2 = int(input('digite outro numero: '))

while num1 + num2 != 50:
    print('A soma nao e 50 tente novamente')
    num1 = int(input('digite um numero: '))
    num2 = int(input('digite outro numero: '))
print('seu numero é 50!!')

