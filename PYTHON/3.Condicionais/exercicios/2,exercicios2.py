"""
Faça um programa que leia um número inteiro fornecido pelo usuário. Se esse número for positivo , calcule a raiz quadrada do número 
e apresente-a. Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.

"""

print('Cálculo de raiz quadrada')
num = int(input('Informe um valor inteiror'))

if num >= 0:
    print(f'O quadrado do valor é {num ** 2}')
else:
    print('Valor inválido')