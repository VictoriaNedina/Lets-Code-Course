#Faça um programa que leia dois números e informe o maior deles.

first_number = float(input("Insira um número: "))
second_number = float(input("Insira outro número: "))

if first_number > second_number:
    print("O maior número é:", first_number)
else:
    print("O maior número é:", second_number)