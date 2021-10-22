#Faça um script que peça ao usuário para digitar um número n e some todos os números de 1 a n.

n = int(input("Digite a quantidade de elementos: "))

cont = 1
result = 0

while cont <= n:
    result += cont
    cont += 1

print(result)