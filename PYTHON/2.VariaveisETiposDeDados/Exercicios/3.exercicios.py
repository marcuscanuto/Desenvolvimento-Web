# Faça um programa que leia 3 valores e apresente a soma dos quadrados dos valores lidos 

print("Somar dos quadrados dos valores")
num1 = int(input("Informe o primeiro valor inteiro"))
num2 = int(input("Informe o segundo valor inteiro"))
num3 = int(input("Informe o terceiro valor inteiro"))

Qnum1 = num1 ** 2
Qnum2 = num2 ** 2
Qnum3 = num3 ** 2

print(f"A soma dos quadrados dos valores informados: {Qnum1+Qnum2+Qnum3}")


# Código otimizado
"""
print("Soma dos quadrados dos valores")
numeros = [int(input(f"Informe o {i+1}º valor inteiro: ")) for i in range(3)]
soma_quadrados = sum(n**2 for n in numeros)
print(f"A soma dos quadrados dos valores informados: {soma_quadrados}")

"""

# Pode colocar assim também -> numero: int = int("informe um número inteiro"). 