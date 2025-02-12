# Tipo numérico

# Pega o inteiro da divisão utilizando o cast 
print(int(5/2))

# Ou pode usar o //
print(5 // 2)

# Pegar o resto 
print(4 % 2)

# Colocar potência usa dois asterisco. Usar somente um é para multiplicação.
print(3 ** 3)

""" Conseguimos separar o número para ver o valor dele, por exemplo 1 milhão 1000000 dessa forma é difícil de visualizar.
    Permite separar as unidade de medida com o underline
"""
print(1_000_000)


num = 42
print(f"imprimindo o valor da variável {num}")

print(f"soma de variável {num + 1}")

# Num recebe num mais um; num = num + 1 ou num +=1
num += 2
print(f" num += 2 -> valor: {num}")

# Num recebe num menos um; num = num - 1 ou num -=1
num -= 2
print(f" num -= 2 -> valor: {num}")

# Outros tipos
num *=2
print(f"num *= 2 -> valor: {num}")

num /= 2
print(f"num /= 2 -> valor: {num}")

print(f"Informa qual o tipo é aquele dado {type(num)}")

print(f"Opção para ver quais opções podemos usar com o tipo de dado na variável num {dir(num)}")