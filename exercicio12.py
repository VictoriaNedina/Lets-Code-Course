#Faça um script que peça para um usuário digitar um número e que só finaliza quando o usuário digitar 0. Ao final imprima a soma de todos os números digitados.

result = 0

while True:
    number = int(input("Digite um número e digite 0 para finalizar: "))
    result += number
    
    if number == 0:
        break

print(result)