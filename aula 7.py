"""
   Módulo exemplo1
   aumento_salarial (salario, percentual)
     REALIZA UM AUMENTO DE SALARIO EM X %
"""


def aumento_salarial(salario, percentual=10):
    novo_salario = salario*percentual/100 + salario
    return novo_salario
salario_fulano = aumento_salarial(5000)
print(salario_fulano)

def reducao_salarial(salario=5000, precentual=10):
    novo_salario = salario - salario*precentual/100
    return novo_salario
    ### abc