# 3.	 Faça um programa com uma função chamada somaImposto.
#  A função possui dois parâmetros formais: taxaImposto,
#   que é a quantia de imposto sobre vendas expressa em porcentagem e custo,
#    que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

def somaImposto(txImposto,custo):
    return txImposto/100*custo + custo

tx = int(input('Informe a tx de imposto: '))
custo = int(input('Informe o custo do produto: '))
print(somaImposto(tx,custo))
