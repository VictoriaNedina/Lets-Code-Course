#Faça um programa que peça 10 números para o usuário e guarde os números em uma lista. Imprima os itens da lista preenchida de trás para frente.

contador = 1
lista = []

while contador <= 10:
    numero = int(input("Digite um número: "))
    contador +=1
    lista.append(numero)

print(lista[::-1])