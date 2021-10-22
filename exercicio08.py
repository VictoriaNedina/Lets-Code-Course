#Uma empresa irá aplicar um reajuste nos salários de seus funcionários de acordo com as seguintes regras:
    #Salário até R$2800,00 (incluindo): aumento de 20%;
    #Salários entre R 2800,00 e R$7000,00: aumento de 15%;
    #Salários entre R 7000,00 e R$15000,00: aumento de 10%;
    #Salários de R$15000,00 em diante: aumento de 5%.
#Dado o salário de um funcionário, informe: o salário antes do reajuste; o percentual de aumento aplicado; o valor do aumento e o novo salário.

salary = float(input("Insira o salário do funcionário em R$ "))

if salary <= 2800:
    percent = 0.2

elif salary <= 7000:
    percent = 0.15

elif salary <= 15000:
    percent = 0.10

else:
    percent = 0.05

readjustment = (salary * percent) + salary
value = readjustment - salary

print("Salário antes do reajuste: R$", salary)
print("Percentual de aumento aplicado:", percent*100,"%")
print("Valor do aumento: R$", value)
print("Novo salário: R$", readjustment)