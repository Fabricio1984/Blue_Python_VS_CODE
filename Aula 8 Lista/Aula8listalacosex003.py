# 3.	Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# •	"Telefonou para a vítima?"
# •	"Esteve no local do crime?"
# •	"Mora perto da vítima?"
# •	"Devia para a vítima?"
# •	"Já trabalhou com a vítima?"  



lista_perguntas = ['Telefonou para a vítima? ','Esteve no local do crime? ','Mora perto da vítima? ','Devia para a vítima? ','Já trabalhou com a vítima? ']

contador = 0
for pergunta in lista_perguntas:
    a = input(pergunta).lower()
    if a == "sim":
        contador += 1

if contador < 2:
    print("Inocente")
elif contador == 2:
    print("Suspeito")
elif contador <= 4:
    print("Cúmplice")
else:
    print("Assassino")