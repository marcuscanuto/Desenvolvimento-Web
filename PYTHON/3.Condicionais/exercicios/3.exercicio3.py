# Faça um programa que recebe um valor inteiro e informa se o valor é par ou impar 

print('Programa - Par ou impar')
valor = int(input('Informe um valor inteiro'))


# Para saber se um valor é par o resto da divisão por 2 deve ser 0
# usamos o dir(valor) e encontramos esse método __mod__ que retorna o resto da divisão
if valor.__mod__(2) == 0:
    print('O valor é par')
else:
    print('O valor é ímpar')
