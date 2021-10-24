# Faça um script que receba um texto de entrada e informe: (i) quantas letras totais (sem espaço), (ii) quantas vogais e (iii) quantas consoantes existem.

texto = (input("Insira seu texto: "))

texto_lower = texto.lower()
texto_sem_espaco = texto_lower.replace(' ', '')
texto_em_lista = list(texto_sem_espaco)

quantidade_letras = len(texto_sem_espaco)
quantidade_vogais = 0

for letra in texto_em_lista:
    if (letra == 'a' or letra == 'á' or letra == 'à' or letra == 'ã' or letra == 'â' or  
        letra == 'e' or letra == 'é' or letra == 'è' or letra == 'ê' or
        letra == 'i' or letra == 'í' or letra == 'ì' or letra == 'î' or
        letra == 'o' or letra == 'ó' or letra == 'ò' or letra == 'õ' or letra == 'ô' or
        letra == 'u' or letra == 'ú' or letra == 'ù' or letra == 'û'):
        quantidade_vogais = quantidade_vogais + 1

quantidade_consoantes = quantidade_letras - quantidade_vogais

print("Quantidade de letras totais (sem espaço): ", quantidade_letras)
print("Quantidade de vogais totais: ", quantidade_vogais)
print("Quantidade de consoantes totais: ", quantidade_consoantes)