#Faça um script que leia números do usuário, enquanto ele não digitar 0. Armazene esses números em uma lista e ao final informe quantos números foram digitados, ignorando o 0.

cont = 1
lista = []

n = float(input("Digite um numero e digite 0 para finalizar): "))

while(n != 0):
    n = float(input("Digite um numero e digite 0 para finalizar): "))
    cont +=1
    
print("Você digitou", (cont-1), "números")