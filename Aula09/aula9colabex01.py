# 1.	Crie um código em Python que pede qual tabuada o usuário quer ver,
#  em seguida imprima essa tabuada.

n = int(input("Digite o número cuja tabuada deseja obter: "))
for i in range(1,11):
    print(n,"x",i,"=",n*i)