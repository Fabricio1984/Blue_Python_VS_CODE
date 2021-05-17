# Exercício 1 - Escreva um programa que pede a senha ao usuário,
#  e só sai do looping quando digitarem corretamente a senha.

senha= 'FSA0511'
entrada = input('Digite sua senha: ')

while entrada != senha:
    print('Senha Incorreta Digite novamente!!')
    entrada = input('Digite sua senha: ')
print('Senha correta pode entar!!')
