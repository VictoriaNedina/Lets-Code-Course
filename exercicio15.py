#Faça um script que informe o fatorial de um número:

numero = float(input("Digite um número para calcular seu fatorial: "))

fatorial = 1

if numero >= 0:
    while(numero >= 1): 
        fatorial *= numero
        numero -= 1
    print(fatorial)

else: 
    print("Não é possível realizar operação com números negativos")