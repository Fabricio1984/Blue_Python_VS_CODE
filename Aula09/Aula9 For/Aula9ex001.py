# 1.	Dada a lista L = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações:
# a.	tamanho da lista.
# b.	maior valor da lista.
# c.	menor valor da lista.
# d.	soma de todos os elementos da lista.
# e.	lista em ordem crescente.
# f.	lista em ordem decrescente.




lista = [5,7,2,9,4,1,3]

tamanho = len(lista)
maior = max(lista)
menor = min(lista)
soma = sum(lista)
lista.sort()
# lista.reverse()

print('tamanho da lista è', tamanho)
print('o maior da lista è', maior)
print('o menor da lista', menor)
print('soma da lista',soma)
print('na ordem crescente da lista',lista)
lista.reverse()
print('lista na ordem decrescente',lista)



