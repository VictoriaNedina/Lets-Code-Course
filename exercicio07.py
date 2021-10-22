#Faça um programa que receba 3 notas de prova de um aluno, calcule a média e diga se ele foi aprovado ou reprovado. A média para aprovação é de pelo menos 6 (aprovado se média maior ou igual a 6).

first_exam = float(input("Insira a primeira nota "))
second_exam = float(input("Insira a segunda nota "))
third_exam = float(input("Insira a terceira nota: "))

media = (first_exam + second_exam + third_exam)/3

if media >= 6:
    print ("Aprovado")
else:
    print("Reprovado")