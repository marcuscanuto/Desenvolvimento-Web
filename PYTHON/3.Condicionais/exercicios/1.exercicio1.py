# Faça um programa que receba dois números inteiros e mostre é o maior
print('Programa - Maior valor')
num1 = int(input('Informe um valor inteiro'))
num2 = int(input('Informe um segundo valor'))

if num1 > num2:
    print(f'O maior valor é: {num1}')
elif num1 == num2:
    print('Os valores informados são iguais')
else:
    print(f'O maior valor é: {num2}')