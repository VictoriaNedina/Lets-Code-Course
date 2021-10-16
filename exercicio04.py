#Faça um script que receba um número e informe: 1) O dobro desse número. 2)O número ao quadrado. 3) O número ao cubo

number = float(input('Digite o número: '))

double = number * 2
squared = number ** 2
cubed = number ** 3

print("O dobro desse número é ", double)
print("O número ao quadrado é ", squared)
print("O número ao cubo é ", cubed)