#Agora faça um script que recebe uma palavra e informa se é um palíndromo, ou seja, se a palavra é igual a ela mesma ao contrário.

text = (input("Digite uma palavra para verificar se é palindromo: "))

lower_text = text.lower()

if lower_text == text[::-1]:
    print("é palindromo")

else:
    print("não é palindromo")