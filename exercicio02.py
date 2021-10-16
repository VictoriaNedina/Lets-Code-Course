#Escreva um programa para ler o salário mensal atual de um funcionário e o percentual de reajuste. Calcular e escrever o valor do novo salário.

salary = float(input('Digite o valor do salário mensal atual: '))

readjustment_percentage = float(input('Digite o percentual de reajuste: '))

new_salary = ((salary * readjustment_percentage) /100) + salary

print("O novo salário é:", new_salary)