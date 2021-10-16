#Faça um programa que peça um nome e a idade que a pessoa fez ou vai fazer esse ano de 2021. Ao final, informe o ano de nascimento dessa pessoa.

name = input("Insira seu nome: ")
age = int(input("Insira sua idade em 2021: "))

birth_date = (2021 - age)

print(name, " nasceu em ", birth_date)