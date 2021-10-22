#Faça um script que peça para o usuário digitar a idade, o salário e o sexo de uma pessoa até que as entradas digitadas sejam válidas.
#    Idade: entre 0 e 150;
#    Salário: maior que 0;
#    Gênero: M, F ou Outro.
#Por último imprima os dados recebidos do usuário.

age = age = int(input("Digite a idade: "))
salary = float(input("Digite o salário: "))
gender = (input("Digite seu sexo: "))

while age < 0 or age >= 150:
    age = int(input("Digite a idade: "))
    
while salary <= 0:
    salary = float(input("Digite o salário: "))

while gender != 'M' and gender != 'F' and gender != 'O':
    gender = (input("Digite seu sexo: "))
    
print("Idade:", age)
print("Salário:", salary)
print("Gênero:", gender)