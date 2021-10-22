#Faça um código que leia um número e informe se ele é par ou ímpar.
number = int(input("Insira um número: "))

if number % 2 == 0:
    print(number, "é par")
else:
    print(number, "é ímpar")