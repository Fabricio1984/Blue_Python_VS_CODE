# Exercício 6 
# Um professor, muito legal, fez 3 provas durante um semestre, mas só vai levar em conta as duas notas mais altas para calcular a média.
# Faça uma aplicação que peça o valor das 3 notas, mostre como seria a média com essas 3 provas, a média com as 2 notas mais altas, bem como sua nota mais alta e sua nota mais baixa.



n = int(input("Entre com o número de matérias: "))

notas = []
for i in range(n):
    nota = float(input("Digite a nota da matéria: "))
    notas.append(nota)

media = sum(notas)/n
print("A média final é: ", str(media))